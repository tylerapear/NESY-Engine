# Animations Class

## Summary

The `Animation` class handles loading, managing, and rendering sprite animations for game entities. It supports multiple animation states, customizable speed, and scaling of images. It also provides visual feedback for entity damage using the `immunity_count` parameter.

---

## Constructor

### Syntax
```python
Animation(spritePath, speed, width, height)
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `spritePath` | str | Yes | N/A | Path to the directory containing sprite images for each animation phase |
| `speed` | int | Yes | N/A | Framerate - speed = how many frames before progressing to the next animation phase (higher = faster animation, up to the framerate) |
| `width` | int | Yes | N/A | Width to scale each loaded image to |
| `height` | int | Yes | N/A | Height to scale each loaded image to |

### Example

```python
animation = Animation("assets/Sprites/Player/Idle", speed=5, width=64, height=64)
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
animation.speed = 10  # Animation updates every 10 frames
```

### `width`
- **Type:** `int`
- **Description:** Get/set image width for scaling

```python
animation.width = 128
```

### `height`
- **Type:** `int`
- **Description:** Get/set image height for scaling

```python
animation.height = 128
```

### `phase`
- **Type:** `int`
- **Description:** Get/set the current animation frame index

### `frame_count`
- **Type:** `int`
- **Description:** Used internally to calculate what how many frames the current_image has been active

### `images`
- **Type:** `list`
- **Description:** The filepath, relative to the project root, of each image in the animation, in the order they are to be drawn

### `current_image`
- **Type:** `pygame.Surface`
- **Description:** The loaded pygame surface of the current image according to `phase`

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

### `update(FRAMERATE, immunity_count = 0)`

Meant to be called once per frame when the animation is active. Sets the animation's current_image according to its speed, phase, framerate, and the immunity_count of the animated entity. Calls helper functions get_damage_phase() and get_image().

**Parameters:**
- `FRAMERATE` (int): The framerate of the game

**Returns:**
- `None`: The method returns None

**Example:**
```python
class Enemy():
    def __init__(self, ...):
        self.current_animation = Animation(...)
    ...

    def update(..., FRAMERATE, ...)
        self.current_animation.update(FRAMERATE, player.immunity_count)
        # ^^^ This is where Animation.update() is called
        # FRAMERATE is passed in from the game loop
    ...
```

### `get_damage_phase(immunity_count)`

Calculates the animation's damage phase based on the provided immunity_count so that the animation is tinted red/white while taking damage

**Parameters:**
- `immunity_count` (int): the imunity_count of the animated entity

**Returns:**
- `DamagePhase`: See notes on the DamagePhase enum in the notes section below

### `get_image(current_image, immunity_count)`

When provided the current_image of the animation, returns a version of the image with the appropriate damage filter applied (if the entity is taking damage) or just returns back the current_image (if the entity is not taking damage)

**Parameters:**
- `current_image` (pygame.Surface): the current image of the animation
- `immunity_count` (int): the imunity_count of the animated entity

**Returns:**
- `pygame.Surface`: returns a version of the current_image

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

```python
player_idle_animation = Animation(spritePath = "assets/Sprites/Player/Idle", ...)
```

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
- Supported image formats: PNG, JPG, JPEG, GIF, BMP
- This module also includes the `DamageMode` enum, with values `NONE`, `FIRST`, `SECOND`, `THIRD`, and `FOURTH`
