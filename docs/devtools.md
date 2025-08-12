---
layout: default
title: Praca z DevTools
nav_order: 20
---

## DevTools — ładowanie i budowanie pluginów

Umieść `DevTools.phar` w `plugins/` serwera, zrestartuj serwer.

### Załaduj plugin z katalogu

Struktura:
```
plugins/
  HelloWorld/
    plugin.yml
    src/
      MyVendor/
        HelloWorld/
          Main.php
```

Restart serwera i plugin ładuje się z katalogu.

### Budowanie do PHAR

```text
/makeplugin HelloWorld --out=plugins
```

Powstanie `plugins/HelloWorld_vX.Y.Z.phar`.

### Rozpakowanie PHAR

```text
/extractplugin HelloWorld
```

### Wskazówki

- Do developingu: DevTools. Do produkcji: Poggit CI.
- Zamiast `/reload` preferuj pełny restart.