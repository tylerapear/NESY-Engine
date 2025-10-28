# Hitbox Class

## Summary
Small rectangle helper used for collision checks and debug drawing. Hitbox provides axis-aligned bounding-box collision detection, a small utility to decide collision side, and optional visible rendering for debugging.

## Constructor

### Syntax
```python
Hitbox(dimentions, visible=False)
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `dimentions` | dict | Yes | N/A | Dictionary with numeric keys: `"x"`, `"y"`, `"width"`, `"height"` specifying the hitbox rectangle. |
| `visible` | bool | No | False | If True the hitbox will be drawn (useful for debugging). |

### Example
```python
hb = Hitbox({"x": 100, "y": 150, "width": 32, "height": 48}, visible=True)
```

---

## Properties

### `x`
- **Type:** `int`
- **Description:** Top-left x coordinate of the hitbox. Update directly to move the hitbox horizontally.

```python
hitbox.x = 100
```

### `y`
- **Type:** `int`
- **Description:** Top-left y coordinate of the hitbox. Update directly to move the hitbox vertically.

```python
hitbox.y = 150
```

### `width`
- **Type:** `int`
- **Description:** Width of the hitbox rectangle in pixels.

```python
hitbox.width = 32
```

### `height`
- **Type:** `int`
- **Description:** Height of the hitbox rectangle in pixels.

```python
hitbox.height = 48
```

### `visible`
- **Type:** `bool`  
- **Description:** When True the hitbox will be drawn for debugging. Typically checked before calling `draw(surface)`.

```python
hitbox.visible = True
if hitbox.visible:
    hitbox.draw(screen)
```

---

## Methods

### `collides(other)`
Returns True if this hitbox intersects the other axis-aligned hitbox.

Parameters:
- `other`: another Hitbox instance

Returns:
- `bool`: True when rectangles overlap

Example:
```python
if my_hitbox.collides(tile.hitbox):
    # handle collision
```

### `getCollisionDirection(other)`
Determines the primary collision side between this hitbox and `other`. The method computes the smallest translation along the X or Y axis required to separate the overlapping rectangles and returns a direction string ("Up", "Down", "Left", or "Right") indicating from which side this hitbox is colliding relative to `other`. This result is suitable for resolving collisions or informing movement/response logic.

Parameters:
- `other`: another Hitbox instance  

Returns:
- `str`: one of "Up", "Down", "Left", "Right"

Example:
```python
collision_side = self.hitbox.getCollisionDirection(tile.hitbox)
```

### `getReverseCollisionDirection(other)`
Determines the primary collision side between this hitbox and `other`. The method computes the smallest translation along the X or Y axis required to separate the overlapping rectangles and returns a direction string ("Up", "Down", "Left", or "Right") indicating from which side `other` is colliding relative to this hitbox. This result is suitable for resolving collisions or informing movement/response logic.

Parameters:
- `other`: another Hitbox instance

Returns:
- `str`: one of "Up", "Down", "Left", "Right"

Example:
```python
collision_side = self.hitbox.getReverseCollisionDirection(tile.hitbox)
```

### `draw(surface, color=(255,0,0), width=1)`
Renders the hitbox rectangle to the provided Pygame surface when `visible` is True. Useful for debugging collisions.

Parameters:
- `surface`: pygame.Surface to draw on
- `color`: RGB tuple for rectangle color (optional)
- `width`: line thickness (optional)

Example:
```python
hitbox.draw(screen)
```

---

## Dependencies
- `pygame` — used for drawing.

---

## Notes
- Use the `visible` flag to toggle debug rendering without changing collision behavior.