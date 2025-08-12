---
layout: default
title: FAQ i typowe błędy
nav_order: 90
---

## Plugin nie ładuje się
- Sprawdź `api: 5.0.0` w `plugin.yml`.
- `main` wskazuje poprawną klasę z namespace.
- Błędy z logów serwera (składnia, brak klas).

## Komenda nie działa
- Zdefiniowana w `plugin.yml` lub zarejestrowana w `onEnable()`?
- `onCommand` zwraca `true` po obsłudze?
- Użytkownik ma odpowiednią permisję?

## Konfiguracja nie zapisuje zmian
- Wywołaj `saveDefaultConfig()` w `onEnable()`.
- Po `set()` wykonaj `save()`.

## Reload vs restart
- Preferuj pełny restart serwera zamiast `/reload` podczas developmentu.