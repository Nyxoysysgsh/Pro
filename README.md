# PMMP AI (RAG TF‑IDF)

Prosty asystent wyszukiwania wiedzy o PocketMine‑MP (API 5) oparty o indeks TF‑IDF.

## Wymagania
- Python 3.10+

## Instalacja
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Użycie
Indeksowanie plików (obsługiwane: .md, .txt, .yml, .yaml, .php):
```bash
python -m src.pmmp_ai.cli ingest docs/ "**/*.md" "**/*.php"
```

Zapytanie:
```bash
python -m src.pmmp_ai.cli ask "jak zarejestrować komendę w pmmp?" --k 5
```

Pliki indeksu są zapisywane w katalogu `vector_store/`.

## Struktura
- `src/pmmp_ai/rag.py` — indeksowanie i wyszukiwanie (TF‑IDF)
- `src/pmmp_ai/cli.py` — interfejs wiersza poleceń

## Uwaga
To minimalna baza. Można rozbudować o: chunking, wagi sekcji, ekstrakcję snippetów i generację odpowiedzi.