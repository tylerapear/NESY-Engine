# Creature Class

## Summary
A class representing an animated creature entity with health, hitbox collision detection, and movement capabilities.

## Constructor

### Syntax
```python
Creature(spritePath, animationSpeed, width=50, height=50, x=0, y=0, hitbox_offset_dimentions={"x-offset": 0, "y-offset": 0, "width": 0, "height": 0}, hitbox_visible=False, alive=True, health=100, display_health=True)
```

### Parameters

| Parameter | Type | Required | Default | Description |
|------------|-------|-----------|--------|--------------|
| `spritePath` | str | Yes | N/A | Filepath to the creature's sprite folder |
| `animationSpeed` | int | Yes | N/A | The speed of the creature's animations |
| `width` | int | No | 50 | Width of the creature in pixels |
| `height` | int | No | 50 | Height of the creature in pixels |
| `x` | int | No | 0 | Starting x position of the creature |
| `y` | int | No | 0 | Starting y position of the creature |
| `hitbox_offset_dimentions` | dict | No | `{"x": 0, "y": 0, "width": 0, "height": 0}` | Offsets for the creature's hitbox dimentions. x and y are additive offsets from the creature's position. width and height are absolute values in pixels for the hitbox size. If x is set to 5, the hitbox will begin 5 pixels after the creature's x position. If width is set to 40, the hitbox will be 40 pixels wide |
| `hitbox_visible` | bool | No | False | Specifies whether the hitbox is visible or not |
| `alive` | bool | No | True | Flag specifying whether or not the creature is currently alive |
| `health` | int | No | 100 | The creature's remaining health value |
| `display_health` | bool | No | True | Specifies whether the creature's health displays |

### Example

```python
creature = Creature(
                spritePath="creature_sprite.png",
                animationSpeed=100,
                width=50,
                height=50,
                x=100,
                y=100,
                hitbox_offset_dimentions={"x": 5, "y": 5, "width": 40, "height": 40},
                hitbox_visible=True,
                alive=True,
                health=100,
                display_health=True
            )
```

---


## Properties

### `x`
- **Type:** `int`
- **Description:** Top-left x coordinate of the creature. Update directly to move the creature horizontally.

```python
creature.x = 150
```

### `y`
- **Type:** `int`
- **Description:** Top-left y coordinate of the creature. Update directly to move the creature vertically.

```python
creature.y = 200
```

### `width`
- **Type:** `int`
- **Description:** Width of the creature rectangle in pixels.

```python
creature.width = 64
```

### `height`
- **Type:** `int`
- **Description:** Height of the creature rectangle in pixels.

```python
creature.height = 64
```

### `direction`
- **Type:** `str`
- **Description:** The direction the creature is currently facing

```python
creature.direction = "right"
```

### `moving`
- **Type:** `bool`
- **Description:** Flag indicating whether the creature is currently moving (used for debugging/testing)

```python
creature.moving = True
```

### `animationPhase`
- **Type:** `int`
- **Description:** Current animation frame phase value

```python
creature.animationPhase = 2
```

### `frame_count`
- **Type:** `int`
- **Description:** Frame counter

```python
creature.frame_count = 0
```

### `immunity_count`
- **Type:** `int`
- **Description:** Timer that counts down the invincibility period after taking damage

```python
creature.immunity_count = 30
```

### `animations`
- **Type:** `Animations`
- **Description:** Manages the creature's sprite animations and frame sequences

```python
creature.animations = Animations(sprite_path)
```

### `current_animation`
- **Type:** `str`
- **Description:** Get/set the name of the currently active animation

```python
creature.current_animation = "walk"
```

### `image`
- **Type:** `pygame.Surface`
- **Description:** Get/set the currently displayed image

```python
creature.image = pygame.image.load("sprite.png")
```

### `hitbox_offset_dimentions`
- **Type:** `dict`
- **Description:** Defines the position offset and size of the hitbox

```python
creature.hitbox_offset_dimentions = {"x": 5, "y": 5, "width": 40, "height": 40}
```

### `hitbox`
- **Type:** `Hitbox`
- **Description:** Hitbox object representing the creature's collision detection area

```python
if creature.hitbox.collides_with(other.hitbox):
    print("Collision detected!")
```

### `alive`
- **Type:** `bool`
- **Description:** Flag indicating whether the creature is alive

```python
creature.alive = True
```

### `movement_locked`
- **Type:** `bool`
- **Description:** When true, the creature is locked in place regardless of input

```python
creature.movement_locked = False
```

### `dying`
- **Type:** `bool`
- **Description:** Flag indicating whether the creature is in a dying state

```python
creature.dying = False
```

### `health`
- **Type:** `int`
- **Description:** The creature's current health value

```python
creature.health = 100
```

### `max_health`
- **Type:** `int`
- **Description:** The creature's maximum health value. This is set to the initial health value when the creature is created and remains constant unless explicitly modified. Useful for calculating health percentages or implementing healing that doesn't exceed the maximum.

```python
creature.max_health = 150
```

### `display_health`
- **Type:** `bool`
- **Description:** When true, displays the creature's current health in the top-left corner

```python
creature.display_health = True
```

### `damage_direction`
- **Type:** `str`
- **Description:** The direction of knockback when damaged

```python
creature.damage_direction = "left"
```

### `up_speed`
- **Type:** `int`
- **Description:** Knockback multiplier for upward direction (1: knockback allowed, 0: knockback blocked by top border/tile collision)

```python
creature.up_speed = 1
```

### `down_speed`
- **Type:** `int`
- **Description:** Knockback multiplier for downward direction (1: knockback allowed, 0: knockback blocked by bottom border/tile collision)

```python
creature.down_speed = 1
```

### `left_speed`
- **Type:** `int`
- **Description:** Knockback multiplier for leftward direction (1: knockback allowed, 0: knockback blocked by left border/tile collision)

```python
creature.left_speed = 1
```

### `right_speed`
- **Type:** `int`
- **Description:** Knockback multiplier for rightward direction (1: knockback allowed, 0: knockback blocked by right border/tile collision)

```python
creature.right_speed = 1
```

---

## Methods

### `update(dt, world_map)`

Updates the creature's state each frame, handling collision detection, health status, animations, and death progression.

**Parameters:**
- `dt`: Delta time (time elapsed since last frame) for frame-independent movement
- `world_map`: The WorldMap object containing the current screen and tile data

**Returns:**
- `None`

**Example:**
```python
creature.update(delta_time, game_world_map)
```

### `draw(surface)`

Renders the creature's current sprite, health display (if enabled), and hitbox (if visible) onto the given surface.

**Parameters:**
- `surface`: pygame.Surface object to draw the creature on

**Returns:**
- `None`

**Example:**
```python
creature.draw(screen)
```

### `moveDirection(dt, direction, speed)`

Moves the creature in the specified direction at the given speed, updating both position and hitbox coordinates.

**Parameters:**
- `dt`: Delta time for frame-independent movement
- `direction`: Direction string ("Up", "Down", "Left", or "Right")
- `speed`: Movement speed in pixels per second

**Returns:**
- `None`

**Example:**
```python
creature.moveDirection(delta_time, "Up", 200)
```

### `moveTo(x, y)`

Instantly teleports the creature to the specified coordinates, updating both sprite and hitbox positions.

**Parameters:**
- `x`: Target x coordinate
- `y`: Target y coordinate

**Returns:**
- `None`

**Example:**
```python
creature.moveTo(300, 400)
```

### `getKnockedBack(dt, direction, speed)`

Applies knockback force to the creature in the specified direction, respecting collision speed multipliers.

**Parameters:**
- `dt`: Delta time for frame-independent movement
- `direction`: Knockback direction ("Up", "Down", "Left", or "Right")
- `speed`: Knockback force in pixels per second

**Returns:**
- `None`

**Example:**
```python
creature.getKnockedBack(delta_time, "Down", 1000)
```

### `takeDamage(damage)`

Reduces the creature's health by the specified damage amount and grants temporary immunity (30 frames).

**Parameters:**
- `damage`: Amount of health to subtract

**Returns:**
- `None`

**Example:**
```python
creature.takeDamage(25)
```

### `handleBorderCollision(world_map, direction)`

Prevents the creature from moving through screen borders by setting the appropriate directional speed multiplier to 0.

**Parameters:**
- `world_map`: The WorldMap object containing screen boundary information
- `direction`: The direction of border collision ("Up", "Down", "Left", or "Right")

**Returns:**
- `None`

**Example:**
```python
creature.handleBorderCollision(game_world, "Up")
```

### `handleTileCollision(direction)`

Prevents the creature from moving through solid tiles by setting the appropriate directional speed multiplier to 0.

**Parameters:**
- `direction`: The direction of tile collision ("Up", "Down", "Left", or "Right")

**Returns:**
- `None`

**Example:**
```python
creature.handleTileCollision("Left")
```

### `progress_death()`

Initiates or continues the death sequence, locking movement and playing the death animation until completion.

**Parameters:**
- None

**Returns:**
- `None`

**Example:**
```python
creature.progress_death()
```

---

## Dependencies
- `pygame`: Used for rendering sprites, surfaces, and health text display
- `Animations`: Manages sprite animations and frame sequences for the creature
- `Hitbox`: Provides collision detection capabilities for the creature

---

## Notes
- The creature uses an immunity system where `immunity_count` provides 30 frames of invincibility after taking damage
- Knockback occurs when immunity_count is greater than 23 (when immunity_count is 30 to 24, total 7 frames)
- Movement is only allowed when immunity_count is less than 18 (movement is disabled when immunity_count is 18 or higher)
- The hitbox offset dimensions use additive offsets for x/y positioning relative to the creature sprite
- When health reaches 0, the creature automatically enters the dying state and plays the "Death" animation if available
- The creature becomes non-alive (`alive = False`) only after the death animation completes
- Speed multipliers (`up_speed`, `down_speed`, `left_speed`, `right_speed`) are reset to 1 each frame and set to 0 during collisions to prevent movement through obstacles