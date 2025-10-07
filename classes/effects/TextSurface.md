Class: TextSurface

Summary:
A Pygame-based class for creating customizable text surfaces with background, borders, padding, and text alignment. It allows developers to overlay styled text on the screen with various visual properties.

Constructor Arguments:

width (int): Width of the text surface in pixels.
    Example: width=300

height (int): Height of the text surface in pixels.
    Example: height=150

x_position (int): X-coordinate of the top-left corner.
    Example: x_position=50

y_position (int): Y-coordinate of the top-left corner.
    Example: y_position=100

background_color (Tuple[int, int, int]): RGB color of the background.
    Example: background_color=(255, 200, 200)

opacity (int): Opacity of the background (0-255).
    Example: opacity=200

visible (bool): Whether the surface is visible.
    Example: visible=False

border_color (Tuple[int, int, int]): RGB color of the border.
    Example: border_color=(0, 100, 0)

border_thickness (int): Thickness of the border in pixels.
    Example: border_thickness=3

border_opacity (int): Opacity of the border (0-255).
    Example: border_opacity=150

padding_top (int): Top padding inside the surface.
    Example: padding_top=20

padding_bottom (int): Bottom padding inside the surface.
    Example: padding_bottom=20

padding_left (int): Left padding inside the surface.
    Example: padding_left=15

padding_right (int): Right padding inside the surface.
    Example: padding_right=15

font_name (str): Name of the font family.
    Example: font_name="Times New Roman"

font_size (int): Size of the font in points.
    Example: font_size=24

font_weight (str): Font weight: "normal" or "bold".
    Example: font_weight="bold"

text_color (Tuple[int, int, int]): RGB color of the text.
    Example: text_color=(255, 0, 0)

horizontal_alignment (str): Text alignment: "left", "center", "right".
    Example: horizontal_alignment="center"

text_content (str): The text string to display.
    Example: text_content="Hello, World!"

surface (Optional[pygame.Surface]): Internal surface (not typically set by user).
    Example: surface=None

Methods:

draw(screen: pygame.Surface): Renders the text surface onto the given screen.
    Example: text_surface.draw(screen)

set_position(x: int, y: int): Sets the x and y position of the surface.
    Example: text_surface.set_position(100, 200)

set_size(width: int, height: int): Sets the width and height of the surface.
    Example: text_surface.set_size(400, 200)

set_padding(top: int, right: int, bottom: int, left: int): Sets all padding values at once.
    Example: text_surface.set_padding(10, 20, 10, 20)

Properties:

width (int): Gets or sets the width of the surface.
    Example: text_surface.width = 350

height (int): Gets or sets the height of the surface.
    Example: text_surface.height = 180

x_position (int): Gets or sets the x position.
    Example: text_surface.x_position = 75

y_position (int): Gets or sets the y position.
    Example: text_surface.y_position = 120

background_color (Tuple[int, int, int]): Gets or sets the background color.
    Example: text_surface.background_color = (0, 255, 0)

opacity (int): Gets or sets the background opacity.
    Example: text_surface.opacity = 128

border_color (Tuple[int, int, int]): Gets or sets the border color.
    Example: text_surface.border_color = (255, 0, 0)

border_thickness (int): Gets or sets the border thickness.
    Example: text_surface.border_thickness = 2

border_opacity (int): Gets or sets the border opacity.
    Example: text_surface.border_opacity = 200

padding_top (int): Gets or sets the top padding.
    Example: text_surface.padding_top = 5

padding_bottom (int): Gets or sets the bottom padding.
    Example: text_surface.padding_bottom = 5

padding_left (int): Gets or sets the left padding.
    Example: text_surface.padding_left = 10

padding_right (int): Gets or sets the right padding.
    Example: text_surface.padding_right = 10

font_name (str): Gets or sets the font name.
    Example: text_surface.font_name = "Courier"

font_size (int): Gets or sets the font size.
    Example: text_surface.font_size = 18

font_weight (str): Gets or sets the font weight.
    Example: text_surface.font_weight = "bold"

text_color (Tuple[int, int, int]): Gets or sets the text color.
    Example: text_surface.text_color = (0, 0, 255)

horizontal_alignment (str): Gets or sets the horizontal alignment.
    Example: text_surface.horizontal_alignment = "right"

text_content (str): Gets or sets the text content.
    Example: text_surface.text_content = "Updated Text"

visible (bool): Gets or sets the visibility.
    Example: text_surface.visible = True