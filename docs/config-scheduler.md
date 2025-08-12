---
layout: default
title: Konfiguracja i scheduler
nav_order: 50
---

## Konfiguracja (`resources/config.yml`)

Przykład:

```yaml
welcomeMessage: "Witaj na serwerze!"
heartbeatIntervalTicks: 20
```

W `onEnable()`:

```php
$this->saveDefaultConfig();
```

Odczyt i zapis:

```php
$value = $this->getConfig()->get("welcomeMessage", "Domyślne");
$this->getConfig()->set("welcomeMessage", "Nowe");
$this->getConfig()->save();
```

## Scheduler

Jednorazowe zadanie za 5 sekund:

```php
$this->getScheduler()->scheduleDelayedTask(new \pocketmine\scheduler\ClosureTask(function() : void {
    $this->getLogger()->info("Minęło 5 sekund.");
}), 20 * 5);
```

Cyklicznie co 2 sekundy:

```php
$this->getScheduler()->scheduleRepeatingTask(new \pocketmine\scheduler\ClosureTask(function() : void {
    // logika cykliczna
}), 40);
```

Wskazówki:
- Używaj `ClosureTask` i typów (API 5).
- Ciężkie operacje przenoś do zadań.