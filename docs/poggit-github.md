---
layout: default
title: Poggit i GitHub Pages
nav_order: 60
---

## Poggit CI (build `.phar`)

1. Utwórz repo GitHub i dodaj pliki pluginu.
2. Dodaj `.poggit.yml` w katalogu głównym repo:

```yaml
branches:
- main

projects:
  HelloWorld:
    path: ""
    icon: "icon.png" # opcjonalnie
```

3. Połącz repo z Poggit i włącz buildy dla gałęzi `main`.
4. Każdy push buduje `.phar`, który można pobrać ze strony projektu.

## GitHub Pages (dokumentacja)

Najprostsza opcja: katalog `docs/` na gałęzi `main` + motyw Just the Docs.

- Plik `docs/_config.yml`:

```yaml
theme: just-the-docs
title: PocketMine‑MP Plugin Dev (API 5)
search_enabled: true
```

- W ustawieniach repo → Pages → Source: `Deploy from a branch` → `Branch: main` → `Folder: /docs`.
- Strona pojawi się pod adresem `https://<login>.github.io/<repo>/`.

## Dodatki

- Odznaki Poggit w `README.md`.
- `CNAME` dla własnej domeny (dodaj plik `docs/CNAME`).