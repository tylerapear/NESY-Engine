# WorldMap Class

## Summary

The WorldMap class manages a grid-based map system composed of multiple screens. It tracks the map dimensions, available screens, and handles navigation between adjacent screens in four directions (Up, Down, Left, Right).

## Constructor

### Syntax

```python
WorldMap(screens_wide, screens_high, screens, start_screen_index)
```

### Parameters

| Parameter            | Type | Required | Default | Description                                                                                                                                         |
| -------------------- | ---- | -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `screens_wide`       | int  | Yes      | N/A     | The number of screens in each row of the map grid                                                                                                   |
| `screens_high`       | int  | Yes      | N/A     | The number of screens in each column of the map grid                                                                                                |
| `screens`            | list | Yes      | N/A     | A list of screen objects representing all screens in the map, ordered left-to-right, top-to-bottom for more info about screen object see screens.md |
| `start_screen_index` | int  | Yes      | N/A     | This must be a valid index from the screens list                                                                                                    |

### Example

```python
# Create a 3x2 map with 6 screens, starting at index 0
# Lets just say we have a array of screen objects in a list which we can feed to worldmap
screens_objects = [screen0, screen1, screen2, screen3, screen4, screen5]
screen_wide = 3
screen_high = 2
current_index = 0
world_map = WorldMap(screen_wide, screen_high, screens_objects, current_index)
```

---

## Properties

### `screens_wide`

-  **Type:** `int`
-  **Description:** The number of screens in each row of the map grid

```python
world_map.screens_wide = 3
```

### `screens_high`

-  **Type:** `int`
-  **Description:** The number of screens in each column of the map grid

```python
world_map.screens_high = 2
```

### `screens`

-  **Type:** `list`
-  **Description:** The list of all screen objects in the map, which we cycle through based on the input given.

```python
world_map.screens = [screen0, screen1, screen2, screen3, screen4, screen5]
```

### `start_screen_index`

-  **Type:** `int`
-  **Description:** The index of the starting screen in the screens list

```python
world_map.start_screen_index = 0
```

### `current_screen`

-  **Type:** `object`
-  **Description:** The screen which is currently active

```python
current = world_map.current_screen
world_map.current_screen = screens[5]
```

---

## Methods

### `setNextScreen(direction)`

Attempts to move to the next screen in the specified direction and sets it as the current screen if valid.

**Parameters:**

-  `direction`: The direction to move. Accepts "Up", "Down", "Left", or "Right", also case sensitive

**Returns:**

-  `object | None`: The next screen object if movement is valid, `None` if at map boundary

**Example:**

```python
# Move to the screen on the right
next_screen = world_map.setNextScreen("Right")
if next_screen:
    print("Moved to new screen")
else:
    print("Cannot move right - at boundary")
```

### `getScreenIfExists(screen_index)`

Safely retrieves a screen by its index, returning None if the index is out of bounds.

**Parameters:**

-  `screen_index`: The index of the screen to retrieve from the screens list

**Returns:**

-  `object | None`: The screen object at the given index, or `None` if the index is invalid

**Example:**

```python
# Get screen at index 5
screen = world_map.getScreenIfExists(5)
if screen:
    print("Screen exists at index 5")
```

### `getNextScreen(direction)`

Calculates and returns the next screen in the specified direction without changing the current screen.

**Parameters:**

-  `direction`: The direction to check. Accepts "Up", "Down", "Left", or "Right"

**Returns:**

-  `object | None`: The next screen object if movement is valid, `None` if at map boundary

**Example:**

```python
# Check if movement down is possible
next_screen = world_map.getNextScreen("Down")
if next_screen:
    print("Can move down to:", next_screen)
else:
    print("At bottom boundary")
```

---

## Notes

-  The screens list should be organized in a grid pattern, ordered left-to-right, top-to-bottom
-  Screen indices start at 0 in the top-left corner
-  For a 3x2 grid, indices are arranged as: [0, 1, 2] in the top row and [3, 4, 5] in the bottom row
-  Navigation methods automatically handle boundary detection to prevent movement outside the map grid
-  The paramaters are case-sensitive, and works only with the 4 given parameter direction types.
