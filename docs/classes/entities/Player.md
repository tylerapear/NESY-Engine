# Player Class

## Summary
The Player class represents the user-controlled character. It inherits from the Creature class and adds player-specific functionalities such as attacking, inventory management, and processing keyboard input. It also overrides the border collision logic to allow for screen transitions.

## Constructor

### Syntax
```python
Player(
  spritePath, 
  animationSpeed, 
  width = 50, 
  height = 50, 
  x = 0, 
  y = 0,
  hitbox_offset_dimentions = {"x": 0, "y": 0, "width": 0, "height": 0},
  hitbox_visible = False,
  alive = True,
  health = 100,
  display_health = True,
  inventory = [ ]
)
```

### Parameters

| Parameter | Type | Required | Default | Description |
|------------|-------|-----------|--------|--------------|
| `spritePath` | str | Yes | N/A | The file path to the sprite sheet or image directory for player animations. |
| `animationSpeed` | float | Yes | N/A | The playback speed of the animations (e.g., 0.1). | 
| `width` | int | No | 50 | The width of the player object. | 
| `height` | int | No | 50 | The height of the player object. | 
| `x` | int | No | 0 | The initial x-coordinate of the player. | 
| `y` | int | No | 0 | The initial y-coordinate of the player. | 
| `hitbox_offset_dimentions` | dict | No | {"x": 0, "y": 0, "width": 0, "height": 0} | A dictionary for the hitbox's position and size offset relative to the sprite. | 
| `hitbox_visible` | bool | No | False | If set to True, draws the hitbox on the screen for debugging. | 
| `alive` | bool | No | True | The initial survival state of the player. | 
| `health` | int | No | 100 | The initial health of the player. | 
| `display_health` | bool | No | True | If set to True, displays a health bar above the player. | 
| `inventory` | list | No | [] | A list to hold items (like weapons) possessed by the player. | 

### Example

```python
import pygame
from classes.entities.Player import Player 
from classes.items.Sword import Sword # Example item

# Create a basic player
player_sprites_path = "assets/sprites/player/"
player = Player(player_sprites_path, 0.1, x=100, y=150)

# Create a player with a custom hitbox and starting item
sword = Sword() # A hypothetical weapon item
hitbox_adj = {"x": 5, "y": 10, "width": -10, "height": -10} # Hitbox adjustment
advanced_player = Player(
    player_sprites_path, 
    0.1, 
    hitbox_offset_dimentions=hitbox_adj, 
    inventory=[sword]
)
```

---


## Properties

### `attacking`
- **Type:** `bool`
- **Description:** Manages the player's current attack state. If True, the attack animation is playing.

```python
if not player.attacking:
    player.attacking = True # Switch to attacking state
```

### `attack_cooldown`
- **Type:** `int`
- **Description:** A frame counter for the attack delay. If this value is greater than 0, the player cannot attack.

```python
if player.attack_cooldown <= 0:
    print("Can attack!")
    player.attack_cooldown = 30 # Set a 30-frame cooldown
```

### `inventory`
- **Type:** `list`
- **Description:** A list containing the item objects possessed by the player.

```python
new_item = Potion() # A hypothetical potion item
player.inventory.append(new_item)
print(f"Current inventory: {player.inventory}")
```

---

## Methods

### `update(dt, screen, surface, enemies, weapon)`

Executes the player's main update logic every frame. Handles input processing, state management, collision detection, animation updates, and more.

**Parameters:**
- `dt`: float - Delta time (time gap since the last frame).
- `screen`: pygame.Surface - (Used by parent class) The main game screen.
- `surface`: pygame.Surface - (Not used) The surface where the game is drawn.
- `enemies`: list - A list of enemy objects. Passed to the checkForDamage method.
- `weapon`: Weapon - The player's currently active weapon object.

**Returns:**
-`None`: The method returns None

**Example:**
```python
# Inside the main game loop
all_enemies = [enemy1, enemy2]
player_sword = player.inventory[0] # Example weapon
dt = clock.tick(60) / 1000.0

player.update(dt, main_screen_surface, game_surface, all_enemies, player_sword)
```

### `draw(surface)`

Draws the player's current sprite (animation) and inventory items (their hitboxes) onto the specified surface.

**Parameters:**
- `surface`: pygame.Surface - The surface where game elements will be drawn.

**Returns:**
- `None`: The method returns None

**Example:**
```python
# In the drawing section of the main game loop
game_surface.fill((0, 0, 0)) # Fill background
player.draw(game_surface) # Draw the player
pygame.display.flip()
```

### `attack(direction, weapon)`

Initiates the player's attack if the attack cooldown is 0 or less.

**Parameters:**
- `direction`: str - The direction the player is facing (e.g., "Up", "Down", "Left", "Right").
- `weapon`: Weapon - The weapon object to be activated.

**Returns:**
-`None`: The method returns None

**Example:**
```python
keys = pygame.key.get_pressed()
if keys[pygame.K_j]: # When 'j' key is pressed
    player.attack(player.direction, player_sword)
```

### `checkForDamage(enemies)`

Iterates through the list of enemies and detects collisions with the player's hitbox. If a collision occurs, it calls the takeDamage method and sets an immunity timer.

**Parameters:**
- `enemies`: list - A list of enemy objects to check for collisions.

**Returns:**
- `None`: The method returns None

**Example:**
```python
# Called automatically inside the update method
# self.checkForDamage(enemies)
```

### `getKnockedBack(dt, direction, speed)`

Overrides the getKnockedBack method from the parent class (Creature). Knocks back the player and also moves any inventory items along with them.

**Parameters:**
- `dt`: float - Delta time.
- `direction`: str - The direction of the knockback.
- `speed`: int or float - The speed of the knockback.

**Returns:**
-`None`: The method returns None

**Example:**
```python
# Called internally by methods like takeDamage
# self.getKnockedBack(dt, "Left", 300)
```

### `checkForGameOver()`

Checks the player's alive attribute to determine if it's a game-over state.

**Parameters:**
- `Parameters`: None

**Returns:**
- `bool`: True if the player is dead (alive == False), otherwise False.

**Example:**
```python
if player.checkForGameOver():
    # Switch to the game over screen
    game_state = "GAME_OVER"
```

### `moveDirection(dt, direction, speed)`

Overrides the moveDirection method from the parent class (Creature). Moves the player and also moves any inventory items along with them.

**Parameters:**
- `dt`: float - Delta time.
- `direction`: str - The direction to move (e.g., "Up", "Down").
- `speed`: int or float - The movement speed.

**Returns:**
- `None`: The method returns None

**Example:**
```python
# Called within the update method based on key input
if keys[pygame.K_w]:
    self.moveDirection(dt, "Up", 200 * self.up_speed)
```

### `moveToNextScreen(world_map, direction)`

Attempts to transition to the next screen in the world_map. If successful, it resets the player's position to an appropriate location on the new screen.

**Parameters:**
- `world_map`: WorldMap - The game's world map object.
- `direction`: str - The direction of the screen to move to.

**Returns:**
- `None`: The method returns None

**Example:**
```python
# Called inside the handleBorderCollision method
# self.moveToNextScreen(world_map, "Up")
```

### `handleBorderCollision(world_map, direction)`

Overrides the handleBorderCollision method from the parent class (Creature). When the player hits a screen border, it calls moveToNextScreen to attempt a screen transition instead of just stopping.

**Parameters:**
- `world_map`: WorldMap - The game's world map object.
- `direction`: str - The direction of the border that was hit.

**Returns:**
- `None`: The method returns None

**Example:**
```python
# Called automatically by the parent class's update logic upon border collision
```

## Dependencies
- `pygame`: Used for keyboard input (pygame.key.get_pressed()) and core game engine functionalities.
- `Creature`: The parent class from which Player inherits core attributes and methods like health, position, animation, basic movement, and damage handling.


## Notes
The Player class relies heavily on the base logic from its parent class, Creature, for movement (moveDirection), damage (takeDamage), and knockback (getKnockedBack).
Movement (WASD) and attack (J) logic are handled directly within the update method through pygame's key input events.
