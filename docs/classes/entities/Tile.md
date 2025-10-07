# Class: Tile
## Summary
Tiles are meant to be placed in an array and used in a [Screen](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Screen.md), which places Tiles in a grid-like arrangement. When put together, tiles form an environment in which [Creatures](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Creature.md) can interact. Tiles contain both a background image, and an optional forground image, the latter of which is meant to be partially transparent. Tiles also include a [Hitbox](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Hitbox.md), which may be active or inactive. Below is an example of an arrangement of Tiles with visible red hitboxes:

<p align="center">
<img width="322" height="239" alt="Screenshot 2025-10-06 170559" src="https://github.com/user-attachments/assets/87844740-e1a6-45b7-bdb5-9329f5b5fbe8" />
</p>

This grid contains "sand" Tiles with inactive hitboxes, and "mountain" Tiles with active hitboxes. Collision logic can then be implemented preventing [Creatures](https://github.com/tylerapear/NESY-Engine/blob/tile-docs/docs/classes/entities/Creature.md) from traveling in "Mountain" Tiles. Three of the "Mountian" Tiles have partially transparent forground images so that the "sand" beneath can be seen.

## Constructor Arguments

### background_img_path

- Required: Yes
- Default: N/A
- Type: String

  A filepath to an image. The Tile constructor will use this path to set the background_image of the Tile:
  
  ```Python
  mountainTile = Tile(
    ...
    background_img_path = "path/to/image.png"
    ...
  )
  ```

### forground_img_path

- Required: No
- Default: ""
- Type: String
  
A filepath to an image. The Tile constructor will use this path to set the forground_image of the Tile:

```Python
mountainTile = Tile(
  ...
  forground_img_path = "path/to/image.png"
  ...
)
```

### hitbox_active

- Required: No
- Default: False
- Type: Boolean
  
Specifies whether the Tile's hitbox is active or not. This property can be used in collision dectection logic:

```Python
mountainTile = Tile(
  ...
  hitbox_active = True # Set to True to allow other objects to collide with the tile's hitbox
  ...
)
```

### hitbox_offset

- Required: No
- Default: {"x": 0, "y": 0, "width": 0, "height": 0}
- Type: Dictionary
  
A filepath to an image. The Tile constructor will use this path to set the forground_image of the Tile:

- x should be in the range 0 - Tile width
- y should be in the range 0 - Tile height
- width should be in the range 0-1
- height should be in the range 0-1

Note: x and y are additive offsets, while width and height are multiplicative offsets. If x is set to 5, the hitbox will begin 5 pixels after the tile begins. If width is set to 0.5, the hitbox will be half as wide as the tile. Here are a couple of examples:

```Python
mountainTile = Tile(
  ...
  hitbox_offset = {"x": 0, "y": 0, "width": 1, "height": 1} # No x or y offset, same height and width as the tile
  ...
)
```

```Python
mountainTile = Tile(
  ...
  hitbox_offset = {"x": 10, "y": 10, "width": 0.2, "height": 0.2} # Slight x and y offset, height and width are 1/5 the height and width of the tile.
  ...
)
```

### hitbox_active

- Required: No
- Default: False
- Type: Boolean
  
Specifies whether the Tile's hitbox is visible or not:

```Python
mountainTile = Tile(
  ...
  hitbox_active = True # Set to True for debugging
  ...
)
```

## Methods
A description and an example for each method
