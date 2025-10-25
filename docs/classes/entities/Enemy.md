# Enemy Class

## Summary
This class implements the [Creature](Creature.md) class to create a generic "Enemy" object type.

## Constructor

### Syntax
```python
Enemy(
    spritePath, animationSpeed, width, height, x, y, hitbox_offset_dimentions, hitbox_visible, alive, health, display_health
)
```

### Parameters

| Parameter | Type | Required | Default | Description |
|------------|-------|-----------|--------|--------------|
| `spritePath` | str | Yes | N/A | Filepath to the enemy's sprite folder |
| `animationSpeed` | int | Yes | N/A | The speed of the enemy's animations |
| `width` | int | No | 50 | Width of the enemy in pixels | 
| `height` | int | No | 50 | Height of the enemy in pixels |
| `x` | int | No | 0 | Starting x position of the enemy |
| `y` | int | No | 0 | Starting y position of the enemy |
| `hitbox_offset_dimentions` | dict | No | {"x-offset": 0, "y-offset": 0, "width": 0, "height": 0} | Offsets for the enemy's hitbox dimentions. x and y are additive offsets, while width and height are multiplicative offsets. If x is set to 5, the hitbox will begin 5 pixels after the enemy's x position. If width is set to 0.5, the hitbox will be half as wide as the enemy |
| `hitbox_visible` | bool | No | False | Specifies whether the hitbox is visible or not |
| `alive` | bool | No | True | Flag specifying whether or not the enemy is currently alive |
| `health` | int | No | 100 | The enemy's remaining health value |
| `display_health` | bool | No | True | Specifies whether the enemy's health displays |

### Example

```python
enemy = Enemy( 
  spritePath = './path/to/sprite/folder', 
  animationSpeed = 25, 
  width = 100, 
  height = 100,
  health = 30,
  x = 1000, 
  y = 500, 
  hitbox_offset_dimentions = {"x": 10, "y": 15, "width": 85, "height": 80}, 
  hitbox_visible = True 
)
```

---


## Properties

No unique properties

See properties of [Creature.py](Creature.md)

---

## Methods

### `update(dt, world_map, weapon)`

This method is meant to be called each frame to update the enemy's state. It calls the update() method of [Creature.py](Creature.md), then handles damage checking.

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
- `Creature`: The Enemy class implements the [Creature](Creature.md) class