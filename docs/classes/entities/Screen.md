# Screen Class

## Constructor

### `Screen(width, height, tiles_wide, tiles_high, tiles, creatures)`

Creates a new Screen instance with specified dimensions and content.

**Parameters:**
- `width` (int): The total width of the screen in pixels
- `height` (int): The total height of the screen in pixels
- `tiles_wide` (int): Number of tiles horizontally across the screen
- `tiles_high` (int): Number of tiles vertically across the screen
- `tiles` (list): List of Tile objects representing the screen layout
- `creatures` (list): List of Creature objects present on this screen

**Example:**
```python
# Create a 256x240 screen (NES resolution) with 16x15 tile grid
screen = Screen(
    width=256,
    height=240,
    tiles_wide=16,
    tiles_high=15,
    tiles=tile_list,
    creatures=creature_list
)
```

# [Class Name] Class

## Summary
The Screen class handles the visual representation of a game level or scene, organizing content into a grid of tiles and managing creatures within the screen boundaries. It provides methods for updating game logic and rendering both background/foreground elements and creatures.

## Constructor

### Syntax
```python
Screen(width, height, tiles_wide, tiles_high, tiles, creatures)
```

### Parameters

| Parameter | Type | Required | Default | Description |
|------------|-------|-----------|--------|--------------|
| `width` | int | Yes | N/A | The width of the screen in pixels |
| `height` | int | Yes | N/A | The height of the screen in pixels |
| `tiles_wide` | int | Yes | N/A | The number of tiles wide the screen is | 
| `tiles_high` | int | Yes | N/A | The number of tiles high the screen is |
| `tiles` | list | Yes | N/A | The list of tiles to be displayed on the screen, sorted first left to right, then top to bottom |
| `creatures` | list | Yes | N/A | The list of creatures on the screen |

### Example

```python
tiles = [Tile(...), Tile(...), ...]
creatures = [JumpingEnemy(...), WanderingEnemy(...)]
screen = Screen(1280, 720, 16, 9, tiles, creatures)
```

---


## Properties

### `width`
- **Type:** `int`
- **Description:** The width of the screen in pixels

```python
screen.width = 1280
```

### `height`
- **Type:** `int`
- **Description:** The height of the screen in pixels

```python
screen.height = 720
```

### `tiles_wide`
- **Type:** `int`
- **Description:** The number of tiles wide the screen is

```python
screen.tiles_wide = 16
```

### `tiles_high`
- **Type:** `int`
- **Description:** The number of tiles high the screen is

```python
screen.tiles_high = 9
```

### `tiles`
- **Type:** `list`
- **Description:** The list of tiles to be displayed on the screen, sorted first left to right, then top to bottom

```python
screen.tiles = [
  Tile(...), #Top left corner
  Tile(...), #Top row, tile 2
  ...,
  Tile(...) #Bottom right corner
]
```

### `creatures`
- **Type:** `list`
- **Description:** The list of creatures on the screen

```python
screen.tiles = [
  WanderingEnemy(...),
  JumpingEnemy(...)
]
```

---

## Methods

### `update(dt, world_map, weapon)`

Meant to be called once per frame in the game loop. Updates the state of the screen and all creatures on the screen.

**Parameters:**
-`dt`: dt (or 'delta time') of the game clock
-`world_map`: The [WorldMap](WorldMap.md) in which the enemy lives
-`weapon`: The weapon that the [Player](Player.md) is currently wielding

**Returns:**
-`None`: The method returns None

**Example:**
```python
dt = clock.tick(60) / 1000
world_map = WorldMap(...)
weapon = Sword(...)

screen.update(dt, world_map, weapon)
```

### `draw(surface, *args, **kwargs)`

Draws the the screen. Starts by drawing tiles, from left to right row by row. Then draws each creature by calling `creature.draw(surface, *args, **kwargs)` for each creature.

**Parameters:**
-`surface`: The pygame surface to draw the screen on

**Returns:**
-`None`: The method returns None

**Example:**
```python
surface = pygame.Surface((1280, 720), pygame.SRCALPHA, 32)
screen.draw(surface)
```

## Dependencies
- None

