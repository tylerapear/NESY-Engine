# Tile Class

## Summary
Tiles are meant to be placed in an array and used in a [Screen](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Screen.md), which places Tiles in a grid-like arrangement. When put together, tiles form an environment in which [Creatures](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Creature.md) can interact. Tiles contain both a background image, and an optional forground image, the latter of which is meant to be partially transparent. Tiles also include a [Hitbox](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Hitbox.md), which may be active or inactive. Below is an example of an arrangement of Tiles with visible red hitboxes:

<p align="center">
<img width="322" height="239" alt="Screenshot 2025-10-06 170559" src="https://github.com/user-attachments/assets/87844740-e1a6-45b7-bdb5-9329f5b5fbe8" />
</p>

## Constructor

### Syntax
```python
Tile(background_img_path, forground_img_path, hitbox_active, hitbox_dimentions, hitbox_offset, hitbox_visible)
```

### Parameters

| Parameter | Type | Required | Default | Description |
|------------|-------|-----------|--------|--------------|
| `background_img_path` | str | Yes | N/A | A filepath to an image. The Tile constructor will use this path to set the background_image of the Tile |
| `forground_img_path` | str | No | "" | A filepath to an image. The Tile constructor will use this path to set the forground_image of the Tile. The forground image is meant to be partially transparent so that the background shows beneath. | 
| `hitbox_active` | bool | No | False | A filepath to an image. Specifies whether the Tile's hitbox is active or not. This property can be used in collision dectection logic | 
| `hitbox_offset` | dict | No | {"x": 0, "y": 0, "width": 0, "height": 0} | Offsets for the tile's hitbox dimentions. x and y are additive offsets, while width and height are multiplicative offsets. If x is set to 5, the hitbox will begin 5 pixels after the tile begins. If width is set to 0.5, the hitbox will be half as wide as the tile |
| `hitbox_visible` | bool | No | False | Specifies whether or not the tile's hitbox is visible. Useful for debugging. |

### Example

```python
tileInstance = Tile(
  background_img_path = "path/to/background/image.png",
  forground_img_path = "path/to/forground/image.png",
  hitbox_active = True,
  hitbox_offset = {"x": 5, "y": 15, "width": 0.5, "height": 0.5},
  hitbox_visible = False
)
```

---


## Properties

### `background_img_path`
- **Type:** `str`
- **Description:**  Get/set filepath to the background image. The Tile constructor will use this path to set the background_image of the Tile

  ```python
  tileInstance.background_img_path = "path/to/background/image.png"
  ```

### `background_image`
- **Type:** `pygame.image`
- **Description:**  Get/set the background image (pygame image).

  ```python
  tileInstance.background_image = pygame.image.load("path/to/background/image.png")
  ```

### `forground_img_path`
- **Type:** `str`
- **Description:** Get/set filepath to the forground image. The Tile constructor will use this path to set the background_image of the Tile. The forground image is meant to be partially transparent so that the background shows beneath.

  ```python
  tileInstance.forground_img_path = "path/to/forground/image.png"
  ```

### `forground_image`
- **Type:** `pygame.image`
- **Description:**  Get/set the forground image (pygame image).

  ```python
  tileInstance.forground_image = pygame.image.load("path/to/forground/image.png")
  ```

### `hitbox_active`
- **Type:** `bool`
- **Description:**  Get/set hitbox_active. Can be used in collision detection logic.

  ```python
  tileInstance.hitbox_active = True
  ```

### `hitbox`
- **Type:** `Hitbox` [See docs](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Hitbox.md)
- **Description:** Get/set the Tile's Hitbox.

  ```python
  tileInstance.hitbox.x = x + tileInstance.hitbox_offset["x"]
  ```

---

## Methods

### `draw_background(screen, surface, x, y)`

Uses pygame to blit the Tile's background_image onto the specified surface with a width and height determined by the specified [screen](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Screen.md)'s tile_width and tile_height.

**Parameters:**
-`screen`: The Screen instance that the Tile is associated with
-`surface`: The pygame surface on which to blit the background image
-`x`: The x position to blit the image
-`y`: The y position to blit the image

**Returns:**
-`None`: None

**Example:**
  ```python

  tileArray = []
  for i in range(1,5):
    tileArray.append(
      Tile(
        "path/to/background/image.png",
        "path/to/forground/image.png",
        True,
        {"x": 0, "y": 0, "width": 1, "height": 1},
        False
      )
    )

  surface = pygame.display.get_surface()
  screen = Screen(
    width = 100,
    height = 100,
    tiles_wide = 2,
    tiles_high = 2,
    tiles = tileArray
  )

  draw_position = [0,0]
  tile_index = 0
  for vertical_tile in range(screen.tiles_high):
    for horizontal_tile in range(screen.tiles_wide):
      tile = screen.tile[tile_index]
      tile.draw_background(screen, surface, draw_position[0], draw_position[1]) # HERE is the method
      draw_position[0] += screen.tile_width
      if tile_index < len(screen.tiles) - 1:
        tile_index += 1
    draw_position[0] = 0
    draw_position[1] += screen.tile_height
  ```

### `draw_forground(screen, surface, x, y)`

Uses pygame to blit the Tile's forground_image onto the specified surface with a width and height determined by the specified [screen](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Screen.md)'s tile_width and tile_height. This is meant to be called after draw_background so that the Tile's forground image is superimposed over the Tile's background image.

**Parameters:**
-`screen`: The Screen instance that the Tile is associated with
-`surface`: The pygame surface on which to blit the forground image
-`x`: The x position to blit the image
-`y`: The y position to blit the image

**Returns:**
-`None`: None

**Example:**
  ```python

  tileArray = []
  for i in range(1,5):
    tileArray.append(
      Tile(
        "path/to/background/image.png",
        "path/to/forground/image.png",
        True,
        {"x": 0, "y": 0, "width": 1, "height": 1},
        False
      )
    )

  surface = pygame.display.get_surface()
  screen = Screen(
    width = 100,
    height = 100,
    tiles_wide = 2,
    tiles_high = 2,
    tiles = tileArray
  )

  # FIRST draw the background

  draw_position = [0,0]
  tile_index = 0
  for vertical_tile in range(screen.tiles_high):
    for horizontal_tile in range(screen.tiles_wide):
      tile = screen.tile[tile_index]
      tile.draw_background(screen, surface, draw_position[0], draw_position[1]) # HERE is the method
      draw_position[0] += screen.tile_width
      if tile_index < len(screen.tiles) - 1:
        tile_index += 1
    draw_position[0] = 0
    draw_position[1] += screen.tile_height

  # THEN draw the forground

  draw_position = [0,0]
  tile_index = 0
  for vertical_tile in range(screen.tiles_high):
    for horizontal_tile in range(screen.tiles_wide):
      tile = screen.tile[tile_index]
      tile.draw_forground(screen, surface, draw_position[0], draw_position[1]) # HERE is the method
      draw_position[0] += screen.tile_width
      if tile_index < len(screen.tiles) - 1:
        tile_index += 1
    draw_position[0] = 0
    draw_position[1] += screen.tile_height
  ```

## Dependencies
- `pygame`: Tile uses pygame to load images into the background_image and forground_image properties.
- `Hitbox`: Tile uses the [Hitbox](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Hitbox.md) class to define the Tile's hitbox.

## Notes
The examples used in draw_background and draw_forground are based on the draw function from [Screen](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Screen.md)
