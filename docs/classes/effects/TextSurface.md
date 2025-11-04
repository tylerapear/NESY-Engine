# TextSurface Class

## Summary
The `TextSurface` class provides a versatile way to display and customize text overlays within a Pygame application. It encapsulates properties for text content, font, color, background, borders, padding, alignment, and opacity, enabling developers to create visually styled text boxes or labels.

## Constructor

### Syntax
```python
TextSurface(
      width = 200,
      height = 100,
      x_position = 0,
      y_position = 0,
      background_color = (255, 255, 255),
      opacity = 255,
      visible = True,
      border_color = (0, 0, 0),
      border_thickness = 1,
      border_opacity = 255,
      padding_top = 10,
      padding_bottom = 10,
      padding_left = 10,
      padding_right = 10,
      font_name = "Arial",
      font_size = 16,
      font_weight = "normal", # "normal", "bold"
      text_color = (0, 0, 0), # Black
      horizontal_alignment = "left",  # "left", "center", "right"
      text_content = "",
      surface = None)
```

### Parameters

| Parameter              | Type         | Required | Default           | Description                                  |
| ---------------------- | ------------ | -------- | ----------------- | -------------------------------------------- |
| `width`                | int          | No       | 200             | The width of the text area.                  |
| `height`               | int          | No       | 100             | The height of the text area.                 |
| `x_position`           | int          | No       | 0               | The X-coordinate of the text area (distance from the left).      |
| `y_position`           | int          | No       | 0               | The Y-coordinate of the text area (distance from the top).       |
| `background_color`     | tuple[int, int, int] | No       | (255, 255, 255) | Background color (RGB format).               |
| `opacity`              | int          | No       | 255             | Background opacity (0 = fully transparent, 255 = opaque).|
| `visible`              | bool         | No       | True            | Whether the element is visible on the screen.|
| `border_color`         | tuple[int, int, int] | No       | (0, 0, 0)       | Border color (RGB format).                   |
| `border_thickness`     | int          | No       | 1               | Border thickness (in pixels).                |
| `border_opacity`       | int          | No       | 255             | Border opacity (0 = transparent, 255 = opaque).|
| `padding_top`          | int          | No       | 10              | Top padding (space between text and area).   |
| `padding_bottom`       | int          | No       | 10              | Bottom padding.                              |
| `padding_left`         | int          | No       | 10              | Left padding.                                |
| `padding_right`        | int          | No       | 10              | Right padding.                               |
| `font_name`            | str          | No       | "Arial"         | Name of the font to use.                     |
| `font_size`            | int          | No       | 16              | Font size (in pt).                           |
| `font_weight`          | str          | No       | "normal"        | Font weight ("normal" or "bold").          |
| `text_color`           | tuple[int, int, int] | No       | (0, 0, 0)       | Text color (RGB format).                     |
| `horizontal_alignment` | str          | No       | "left"          | Horizontal alignment of the text ("left", "center", "right").|
| `text_content`         | str          | No       | ""              | Text content to display.                     |
| `surface`              | pygame.Surface | No       | None            | Target Surface object where text will be rendered. |


### Example

```python
# Create a basic text box
text_box = TextSurface(
    width=300,
    height=50,
    x_position=10,
    y_position=10,
    text_content="Hello, Pygame!"
)

# Create a styled text box
styled_box = TextSurface(
    width=200, height=100, x_position=50, y_position=70,
    background_color=(50, 50, 50),
    opacity=200,
    border_color=(255, 0, 0),
    border_thickness=3,
    text_content="Centered Text",
    text_color=(255, 255, 255),
    font_size=20,
    horizontal_alignment="center"
)
```

---


## Properties

### `width`
- **Type:** `int`
- **Description:** The width of the text surface.

### `height`
- **Type:** `int`
- **Description:** The height of the text surface.

### `x_position`
- **Type:** `int`
- **Description:** The x-coordinate of the top-left corner of the text surface.

### `y_position`
- **Type:** `int`
- **Description:** The y-coordinate of the top-left corner of the text surface.

### `background_color`
- **Type:** `Tuple[int, int, int]`
- **Description:** The RGB background color of the text surface.

### `opacity`
- **Type:** `int`
- **Description:** The opacity of the background (0-255).

### `visible`
- **Type:** `bool`
- **Description:** Controls whether the surface is rendered.

### `border_color`
- **Type:** `Tuple[int, int, int]`
- **Description:** The RGB color of the border.

### `border_thickness`
- **Type:** `int`
- **Description:** The thickness of the border in pixels.

### `border_opacity`
- **Type:** `int`
- **Description:** The opacity of the border (0-255).

### `padding_top`
- **Type:** `int`
- **Description:** The top padding within the surface.

### `padding_bottom`
- **Type:** `int`
- **Description:** The bottom padding within the surface.

### `padding_left`
- **Type:** `int`
- **Description:** The left padding within the surface.

### `padding_right`
- **Type:** `int`
- **Description:** The right padding within the surface.

### `font_name`
- **Type:** `str`
- **Description:** The name of the font to use.

### `font_size`
- **Type:** `int`
- **Description:** The size of the font.

### `font_weight`
- **Type:** `str`
- **Description:** The weight of the font ("normal" or "bold").

### `text_color`
- **Type:** `Tuple[int, int, int]`
- **Description:** The RGB color of the text.

### `horizontal_alignment`
- **Type:** `str`
- **Description:** The horizontal alignment of the text ("left", "center", or "right").

### `text_content`
- **Type:** `str`
- **Description:** The text content to display.

---

## Methods

### `draw(screen)`

Renders the text surface onto a given Pygame screen.

**Parameters:**
- `screen` (`pygame.Surface`): The Pygame surface to draw on.

**Returns:**
- `None`

**Example:**
```python
my_text_surface.draw(game_screen)
```

### `set_position(x, y)`

Sets the x and y position of the text surface.

**Parameters:**
- `x` (`int`): The new x-coordinate.
- `y` (`int`): The new y-coordinate.

**Returns:**
- `None`

**Example:**
```python
my_text_surface.set_position(100, 150)
```

### `set_size(width, height)`

Sets the width and height of the text surface.

**Parameters:**
- `width` (`int`): The new width.
- `height` (`int`): The new height.

**Returns:**
- `None`

**Example:**
```python
my_text_surface.set_size(300, 100)
```

### `set_padding(top, right, bottom, left)`

Sets the padding for all sides of the text surface.

**Parameters:**
- `top` (`int`): The top padding.
- `right` (`int`): The right padding.
- `bottom` (`int`): The bottom padding.
- `left` (`int`): The left padding.

**Returns:**
- `None`

**Example:**
```python
my_text_surface.set_padding(10, 20, 10, 20)
```

## Dependencies
- `pygame`: Used for creating surfaces, drawing, and handling fonts.

## Notes
- The `font_weight` property must be either "normal" or "bold".
- Opacity values range from 0 (fully transparent) to 255 (fully opaque).
- The `horizontal_alignment` property must be one of "left", "center", or "right".
- The `font_size` must be a positive integer.
- `width`, `height`, `border_thickness`, and padding values cannot be negative.
