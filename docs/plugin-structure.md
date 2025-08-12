---
layout: default
title: Struktura pluginu
nav_order: 30
---

## Podstawowa struktura

```
plugins/
  HelloWorld/
    plugin.yml
    src/
      MyVendor/
        HelloWorld/
          Main.php
    resources/
      config.yml
```

### Przykładowy `plugin.yml`

```yaml
name: HelloWorld
main: MyVendor\HelloWorld\Main
version: 1.0.0
api: 5.0.0
author: TwojeImie
description: Pierwszy plugin dla PMMP
commands:
  hello:
    description: Przywitaj się
    usage: "/hello"
    permission: helloworld.use
permissions:
  helloworld.use:
    default: true
    description: Pozwala użyć /hello
```

### Minimalny `Main.php`

```php
<?php

declare(strict_types=1);

namespace MyVendor\HelloWorld;

use pocketmine\plugin\PluginBase;
use pocketmine\event\Listener;
use pocketmine\event\player\PlayerJoinEvent;
use pocketmine\command\Command;
use pocketmine\command\CommandSender;
use pocketmine\player\Player;
use pocketmine\scheduler\ClosureTask;
use pocketmine\utils\TextFormat as TF;

final class Main extends PluginBase implements Listener
{
    protected function onEnable() : void
    {
        $this->getServer()->getPluginManager()->registerEvents($this, $this);
        $this->getScheduler()->scheduleRepeatingTask(new ClosureTask(function () : void {
            // logika cykliczna
        }), 20);
        $this->saveDefaultConfig();
    }

    public function onPlayerJoin(PlayerJoinEvent $event) : void
    {
        $player = $event->getPlayer();
        $player->sendMessage(TF::GREEN . "Witaj, " . $player->getName() . "!");
    }

    public function onCommand(CommandSender $sender, Command $command, string $label, array $args) : bool
    {
        if ($command->getName() === "hello") {
            if (!$sender->hasPermission("helloworld.use")) {
                $sender->sendMessage(TF::RED . "Brak uprawnień.");
                return true;
            }
            $name = $sender instanceof Player ? $sender->getName() : "konsola";
            $sender->sendMessage(TF::YELLOW . "Hello, {$name}!");
            return true;
        }
        return false;
    }
}
```