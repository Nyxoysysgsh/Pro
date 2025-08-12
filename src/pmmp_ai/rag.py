from __future__ import annotations

import os
import json
import pathlib
from dataclasses import dataclass
from typing import List, Dict, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

SUPPORTED_EXT = {".md", ".txt", ".yml", ".yaml", ".php"}


def read_text_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""


@dataclass
class Document:
    doc_id: str
    path: str
    text: str


class TfidfRag:
    def __init__(self, vector_store_dir: str) -> None:
        self.vector_store_dir = pathlib.Path(vector_store_dir)
        self.vector_store_dir.mkdir(parents=True, exist_ok=True)
        self.index_path = self.vector_store_dir / "index.npz"
        self.meta_path = self.vector_store_dir / "meta.json"
        self.vectorizer_path = self.vector_store_dir / "vectorizer.json"

        self.vectorizer: TfidfVectorizer | None = None
        self.matrix: np.ndarray | None = None
        self.meta: List[Dict] = []

    def _save(self) -> None:
        assert self.vectorizer is not None and self.matrix is not None
        # Save sparse matrix as npz
        from scipy import sparse
        sparse.save_npz(self.index_path, self.matrix)

        # Save metadata
        with open(self.meta_path, "w", encoding="utf-8") as f:
            json.dump(self.meta, f, ensure_ascii=False, indent=2)

        # Save vectorizer vocabulary and config
        vec_data = {
            "vocabulary_": self.vectorizer.vocabulary_,
            "idf_": self.vectorizer.idf_.tolist(),
            "stop_words_": list(self.vectorizer.stop_words_ or []),
            "lowercase": self.vectorizer.lowercase,
            "ngram_range": self.vectorizer.ngram_range,
            "max_df": self.vectorizer.max_df,
            "min_df": self.vectorizer.min_df,
        }
        with open(self.vectorizer_path, "w", encoding="utf-8") as f:
            json.dump(vec_data, f)

    def _load(self) -> bool:
        if not (self.index_path.exists() and self.meta_path.exists() and self.vectorizer_path.exists()):
            return False
        from scipy import sparse
        self.matrix = sparse.load_npz(self.index_path)
        with open(self.meta_path, "r", encoding="utf-8") as f:
            self.meta = json.load(f)
        with open(self.vectorizer_path, "r", encoding="utf-8") as f:
            vec_data = json.load(f)
        vec = TfidfVectorizer(lowercase=vec_data.get("lowercase", True),
                               ngram_range=tuple(vec_data.get("ngram_range", (1, 2))),
                               max_df=vec_data.get("max_df", 0.9),
                               min_df=vec_data.get("min_df", 1))
        # Rebuild vectorizer
        vec.vocabulary_ = {k: int(v) for k, v in vec_data["vocabulary_"].items()}
        vec.idf_ = np.array(vec_data["idf_"])  # type: ignore[attr-defined]
        vec._tfidf._idf_diag = None  # type: ignore[attr-defined]
        self.vectorizer = vec
        return True

    def ingest_paths(self, paths: List[str], glob: bool = True) -> int:
        files: List[str] = []
        for p in paths:
            if glob and any(x in p for x in ["*", "?"]):
                for fp in pathlib.Path().glob(p):
                    if fp.suffix.lower() in SUPPORTED_EXT and fp.is_file():
                        files.append(str(fp))
            else:
                pth = pathlib.Path(p)
                if pth.is_dir():
                    for fp in pth.rglob("*"):
                        if fp.suffix.lower() in SUPPORTED_EXT and fp.is_file():
                            files.append(str(fp))
                elif pth.is_file() and pth.suffix.lower() in SUPPORTED_EXT:
                    files.append(str(pth))
        files = sorted(set(files))
        docs: List[Document] = []
        for i, fpath in enumerate(files):
            text = read_text_file(fpath)
            if not text.strip():
                continue
            docs.append(Document(doc_id=str(i), path=fpath, text=text))
        if not docs:
            return 0
        corpus = [d.text for d in docs]
        vec = TfidfVectorizer(lowercase=True, ngram_range=(1, 2), max_df=0.9, min_df=1)
        matrix = vec.fit_transform(corpus)
        self.vectorizer = vec
        self.matrix = matrix
        self.meta = [{"doc_id": d.doc_id, "path": d.path} for d in docs]
        self._save()
        return len(docs)

    def query(self, question: str, top_k: int = 5) -> List[Tuple[float, Dict]]:
        if self.vectorizer is None or self.matrix is None:
            if not self._load():
                return []
        assert self.vectorizer is not None and self.matrix is not None
        q_vec = self.vectorizer.transform([question])
        sims = cosine_similarity(q_vec, self.matrix).flatten()
        idx = np.argsort(-sims)[:top_k]
        results: List[Tuple[float, Dict]] = []
        for i in idx:
            score = float(sims[i])
            meta = self.meta[int(i)] if i < len(self.meta) else {}
            results.append((score, meta))
        return results