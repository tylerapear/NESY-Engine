# Screen

**File Location:** `lib/classes/entities/Screen.py`

The `Screen` class represents a game screen in an NES-style game, managing tile-based rendering, creature updates, and display properties for a grid-based game world.

## Description

The Screen class handles the visual representation of a game level or scene, organizing content into a grid of tiles and managing creatures within the screen boundaries. It provides methods for updating game logic and rendering both background/foreground elements and creatures.

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
