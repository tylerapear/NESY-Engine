# Animations Class

## Summary

The `Animations` class handles loading, managing, and rendering sprite animations for game entities. It supports multiple animation states, customizable speed, and scaling of images. It also provides visual feedback for entity damage using the `immunity_count` parameter.

---

## Constructor

### Syntax
```python
Animations(spritePath, speed, width, height)
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `spritePath` | str | Yes | N/A | Path to the directory containing sprite subfolders for each animation state |
| `speed` | int | Yes | N/A | Number of frames before switching to the next image (higher = slower animation) |
| `width` | int | Yes | N/A | Width to scale each loaded image to |
| `height` | int | Yes | N/A | Height to scale each loaded image to |

### Example

```python
animations = Animations("assets/Sprites/Player", speed=5, width=64, height=64)
```

---

## Properties

### `spritePath`
- **Type:** `str`
- **Description:** Get/set the path to the sprite directory

### `speed` 
- **Type:** `int`
- **Description:** Get/set animation speed (frames per image change)

```python
animations.speed = 10  # Animation updates every 10 frames
```

### `width`
- **Type:** `int`
- **Description:** Get/set image width for scaling

```python
animations.width = 128
```

### `height`
- **Type:** `int`
- **Description:** Get/set image height for scaling

```python
animations.height = 128
```

### `phase`
- **Type:** `int`
- **Description:** Get/set the current animation frame index

### `animations`
- **Type:** `dict`
- **Description:** Get/set dictionary of loaded animations

### `current_animation`
- **Type:** `str`
- **Description:** Get/set the name of the currently active animation

```python
animations.current_animation = "Run"
print(animations.phase)
```

### `image`
- **Type:** `pygame.Surface`
- **Description:** Get/set the currently displayed image

---

## Methods

### `load_animations(root_dir)`

Loads all images from subdirectories of `root_dir`. Each subdirectory represents an animation state.

**Parameters:**
- `root_dir` (str): Directory containing animation subfolders

**Returns:**
- `dict`: Dictionary of animation images keyed by animation state name

**Example:**
```python
animations_dict = animations.load_animations("assets/Sprites/Player")
print(animations_dict["Idle"])  # List of file paths for Idle animation
```

### `getNextImage(entity, immunity_count=0)`

Updates the animation frame for a given entity and returns the next image. Handles animation phase changes, frame counting, and optional immunity/damage visual effects.

**Parameters:**
- `entity`: Game entity object with a `current_animation` attribute
- `immunity_count` (int, optional): Counter for damage immunity frames. Creates flashing red effect when > 0. Default is 0.

**Returns:**
- `pygame.Surface`: The next animation frame

**Example:**
```python
player_image = animations.getNextImage(player_entity, immunity_count=20)
screen.blit(player_image, (player_x, player_y))
```

---

## Usage Example

```python
import pygame
from Animations import Animations

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Initialize animations
player_anim = Animations("assets/Sprites/Player", speed=5, width=64, height=64)
player_entity = type("Entity", (), {})()  # Simple mock object
player_entity.current_animation = "Idle"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Update player animation
    player_image = player_anim.getNextImage(player_entity)
    screen.blit(player_image, (100, 100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

---

## Directory Structure

Your sprite directory should be organized as follows:

```
assets/Sprites/Player/
├── Idle/
│   ├── frame_01.png
│   ├── frame_02.png
│   └── frame_03.png
├── Run/
│   ├── frame_01.png
│   ├── frame_02.png
│   └── frame_03.png
└── Jump/
    ├── frame_01.png
    └── frame_02.png
```

---

## Animation States

The class automatically detects animation states based on subfolder names in the sprite directory:

- Each subfolder becomes an animation state
- Subfolder names are case-sensitive
- Images within subfolders are loaded in alphabetical order
- Supported image formats: PNG, JPG, JPEG, GIF, BMP

---

## Performance Notes

- Images are loaded once during initialization and cached in memory
- Animation frame switching is based on frame counting, not time
- Scaling operations are performed during loading, not during rendering
- The `immunity_count` effect applies a red color overlay without modifying the original image

---

## Dependencies

- **pygame**: Required for image loading, scaling, and surface operations
- **os**: Used for directory traversal and file path operations

---

## Notes

- Each subfolder name becomes an animation state (e.g., "Idle", "Run", "Jump")
- Images are loaded and scaled automatically based on constructor parameters
- Animation speed is controlled by the `speed` parameter - higher values create slower animations
- The `immunity_count` parameter enables damage feedback by applying visual effects to the sprite
- All images are converted to pygame surfaces for optimal rendering performance
