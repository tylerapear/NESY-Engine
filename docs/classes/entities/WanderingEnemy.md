# WanderingEnemy Class

## Summary
A class that implements [Enemy.py](Enemy.md) and creates an enemy that randomly wanders around the screen.

## Constructor

No unique constructor

See constructor of [Enemy.py](Enemy.md)

---


## Properties

No unique properties

See properties of [Enemy.py](Enemy.md)

---

## Methods

See methods of [Enemy.py](Enemy.md), and:

### `update(dt, world_map, weapon)`

This method is meant to be called each frame to update the wandering enemy's state. It calls the update() method of [Creature.py](Creature.md), then handles wandering AI, then handles damage checking.

**Parameters:**
-`dt`: dt (or 'delta time') of the game clock
-`world_map`: The [WorldMap](WorldMap.md) in which the enemy lives
-`weapon`: The weapon that the [Player](Player.md) is currently wielding

**Returns:**
-`None`: The method returns None

**Example:**
```python
player = Player(...)
world_map = WorldMap(...)
player.inventory.append(Sword(...))

enemy.update(dt, world_map, player.inventory[0])
```

## Dependencies
- `Creature`: The WanderingEnemy class uses the update() function of the [Creature](Creature.md) class
- `Enemy`: The WanderingEnemy class implements the [Enemy](Enemy.md) class