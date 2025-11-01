# LogicalSurface Class

## Summary
LogicalSurface is a helper class that wraps Pygame's `Surface` object. It represents a "logical" screen area and provides functionality to render this logical surface onto a "physical" screen of a different size, automatically scaling and centering it while maintaining the aspect ratio.

## Constructor

### Syntax
```python
LogicalSurface(width, height, background_color)
```

### Parameters

| Parameter | Type | Required | Default | Description |
|------------|-------|-----------|--------|--------------|
| `width` | int | Yes | N/A | The logical width of the surface. |
| `height` | int | Yes | N/A | The logical height of the surface. |
| `background_color` | tuple | Yes | N/A | The background color of the surface in RGB format (e.g., (0,0,0)). |


### Example

```python
import pygame
from classes.entities.LogicalSurface import LogicalSurface

pygame.init()

# Create a logical surface 800x600 with white background.
logical_surface = LogicalSurface(800,600,(255, 255, 255))
```

---


## Properties

### `surface`
- **Type:** `pygame.Surface`
- **Description:** The internal Pygame 'surface' instance managed by this class. All game elements should be drawn onto this surface.

```python
# Access the internal surface and fill it with red.
internal_surf = logical_surface.surface
internal_surf.fill((255,0,0))
```
### `width`
- **Type:** `int`
- **Description:** The logical width of the surface.

```python
# Get the logical width
w = logical_surface.width
print(f"Logical width: {w}")
```
### `height`
- **Type:** `int`
- **Description:** The logical height of the surface.

```python
# Get the logical height 
h = logical_surface.height
print(f"Logical height: {h}")
```
### `background_color`
- **Type:** `tuple`
- **Description:** The background color of the surface in RGB format.

```python
# Get the background color 
color = logical_surface.background_color
print(f"Background color : {color}") # Background color : (255,255,255)
```
---

## Methods

### `compute_fit(dst_w, dst_h)`

Calculates the scale, offsets, and render dimensions required to fit the logical surface onto a destination surface while maintaining the aspect ratio.

**Parameters:**
-`dst_w` (int): The width of the destination surface. 
-`dst_h` (int): The height of the destination surface.

**Returns:**
- `tuple` : A tuple containing `(scale, x_off, y_off, render_w, render_h)`
    - `scale` (float): The scaling ratio to be applied.
    - `x_off` (int): The X-axis offset on the destination surface (for centering).
    - `y_off` (int): The Y-axis offset on the destination surface (for centering).
    - `render_w` (int): The final rendered width after scaling.
    - `render_h` (int): The final rendered height after scaling.

**Example:**
```python
scale, x_off, y_off, render_w, render_h = logical_surface.compute_fit(1920,1080)
print(f"Scale: {scale}, Offset: ({x_off}, {y_off}), Render Size: ({render_w}, {render_h})")
```

### `blit(surface)`

Renders (blits) the logical surface onto a target `pygame.Surface`. This method first fills the target surface with the background_color, then draws the scaled logical surface onto the center of the target.

**Parameters:**
-`surface` (pygame.Surface): The destination surface to draw onto.

**Returns:**
- `None`.

**Example:**
```python
# Create the main display surface.
screen = pygame.display.set_mode((1280, 720))
# Draw a blue rectangle on the logical surface.
pygame.draw.rect(logical_surface.surface, (0, 0, 255), (100, 100, 50, 50))
# Render (blit) the logical surface to the display.
logical_surface.blit(screen)
pygame.display.flip()
```

## Dependencies
-`pygame`: Used for Surface creation, scaling and rendering.

## Notes
- This class is a wrapper to simplify resolution-independent rendering.
- You can access the internal surface through the `surface` property to draw or modify its content directly - for example, filling the logical surface with a color or rendering extra elements before blitting.
- The intended workflow is to draw all your game elements onto the `LogicalSurface.surface` first, and then call `LogicalSurface.blit()` once per frame to render the entire scaled scene to the main display.