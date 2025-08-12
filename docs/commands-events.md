---
layout: default
title: Komendy i eventy
nav_order: 40
---

## Rejestracja komend

### W `plugin.yml`

```yaml
commands:
  hello:
    description: Przywitaj się
    usage: "/hello"
    permission: helloworld.use
```

### Własna klasa komendy

```php
use pocketmine\command\Command;
use pocketmine\command\CommandSender;
use pocketmine\command\utils\InvalidCommandSyntaxException;

final class HelloCommand extends Command {
    public function __construct() {
        parent::__construct("hello", "Przywitaj się", "/hello [nick]");
        $this->setPermission("helloworld.use");
    }

    public function execute(CommandSender $sender, string $label, array $args) : bool {
        if (!$this->testPermission($sender)) return true;
        $target = $args[0] ?? $sender->getName();
        if (($args[0] ?? '') === "?") throw new InvalidCommandSyntaxException();
        $sender->sendMessage("Hello, {$target}!");
        return true;
    }
}
```

Rejestracja w `onEnable()`:

```php
$this->getServer()->getCommandMap()->register("helloworld", new HelloCommand());
```

## Eventy

Rejestracja:

```php
$this->getServer()->getPluginManager()->registerEvents($this, $this);
```

Przykład blokowania niszczenia bloków bez permisji:

```php
use pocketmine\event\block\BlockBreakEvent;

public function onBlockBreak(BlockBreakEvent $event) : void {
    $player = $event->getPlayer();
    if (!$player->hasPermission("helloworld.break")) {
        $event->cancel();
        $player->sendMessage("Nie możesz niszczyć bloków.");
    }
}
```

`plugin.yml`:

```yaml
permissions:
  helloworld.break:
    default: op
```