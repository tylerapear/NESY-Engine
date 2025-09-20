import pygame
from typing import Tuple, Optional

class TextSurface:
    """
    A class that allows developers to overlay text on the screen with customizable properties.
    """
    
    def __init__(self):
        # Surface properties (private)
        self._width = 200
        self._height = 100
        self._x_position = 0
        self._y_position = 0
        self._background_color = (255, 255, 255)  # White
        self._opacity = 255
        self._visible = True
        
        # Border properties (private)
        self._border_color = (0, 0, 0)  # Black
        self._border_thickness = 1
        self._border_opacity = 255
        
        # Padding properties (private)
        self._padding_top = 10
        self._padding_bottom = 10
        self._padding_left = 10
        self._padding_right = 10
        
        # Text properties (private)
        self._font_name = "Arial"
        self._font_size = 16
        self._font_weight = "normal"  # "normal", "bold"
        self._text_color = (0, 0, 0)  # Black
        self._horizontal_alignment = "left"  # "left", "center", "right"
        self._text_content = ""
        
        # Internal surface
        self._surface = None
        self._font = None
        self._update_font()
    
    def _update_font(self):
        """Update the pygame font object when font properties change."""
        bold = self._font_weight == "bold"
        self._font = pygame.font.SysFont(self._font_name, self._font_size, bold=bold)
    
    # Width property
    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, value: int):
        self._width = max(0, value)
    
    # Height property
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, value: int):
        self._height = max(0, value)
    
    # X Position property
    @property
    def x_position(self) -> int:
        return self._x_position
    
    @x_position.setter
    def x_position(self, value: int):
        self._x_position = value
    
    # Y Position property
    @property
    def y_position(self) -> int:
        return self._y_position
    
    @y_position.setter
    def y_position(self, value: int):
        self._y_position = value
    
    # Background Color property
    @property
    def background_color(self) -> Tuple[int, int, int]:
        return self._background_color
    
    @background_color.setter
    def background_color(self, value: Tuple[int, int, int]):
        self._background_color = value
    
    # Opacity property
    @property
    def opacity(self) -> int:
        return self._opacity
    
    @opacity.setter
    def opacity(self, value: int):
        self._opacity = max(0, min(255, value))
    
    # Border Color property
    @property
    def border_color(self) -> Tuple[int, int, int]:
        return self._border_color
    
    @border_color.setter
    def border_color(self, value: Tuple[int, int, int]):
        self._border_color = value
    
    # Border Thickness property
    @property
    def border_thickness(self) -> int:
        return self._border_thickness
    
    @border_thickness.setter
    def border_thickness(self, value: int):
        self._border_thickness = max(0, value)
    
    # Border Opacity property
    @property
    def border_opacity(self) -> int:
        return self._border_opacity
    
    @border_opacity.setter
    def border_opacity(self, value: int):
        self._border_opacity = max(0, min(255, value))
    
    # Padding properties
    @property
    def padding_top(self) -> int:
        return self._padding_top
    
    @padding_top.setter
    def padding_top(self, value: int):
        self._padding_top = max(0, value)
    
    @property
    def padding_bottom(self) -> int:
        return self._padding_bottom
    
    @padding_bottom.setter
    def padding_bottom(self, value: int):
        self._padding_bottom = max(0, value)
    
    @property
    def padding_left(self) -> int:
        return self._padding_left
    
    @padding_left.setter
    def padding_left(self, value: int):
        self._padding_left = max(0, value)
    
    @property
    def padding_right(self) -> int:
        return self._padding_right
    
    @padding_right.setter
    def padding_right(self, value: int):
        self._padding_right = max(0, value)
    
    # Font Name property
    @property
    def font_name(self) -> str:
        return self._font_name
    
    @font_name.setter
    def font_name(self, value: str):
        self._font_name = value
        self._update_font()
    
    # Font Size property
    @property
    def font_size(self) -> int:
        return self._font_size
    
    @font_size.setter
    def font_size(self, value: int):
        self._font_size = max(1, value)
        self._update_font()
    
    # Font Weight property
    @property
    def font_weight(self) -> str:
        return self._font_weight
    
    @font_weight.setter
    def font_weight(self, value: str):
        if value in ["normal", "bold"]:
            self._font_weight = value
            self._update_font()
    
    # Text Color property
    @property
    def text_color(self) -> Tuple[int, int, int]:
        return self._text_color
    
    @text_color.setter
    def text_color(self, value: Tuple[int, int, int]):
        self._text_color = value
    
    # Horizontal Alignment property
    @property
    def horizontal_alignment(self) -> str:
        return self._horizontal_alignment
    
    @horizontal_alignment.setter
    def horizontal_alignment(self, value: str):
        if value in ["left", "center", "right"]:
            self._horizontal_alignment = value
    
    # Text Content property
    @property
    def text_content(self) -> str:
        return self._text_content
    
    @text_content.setter
    def text_content(self, value: str):
        self._text_content = value
    
    # Visibility property
    @property
    def visible(self) -> bool:
        return self._visible
    
    @visible.setter
    def visible(self, value: bool):
        self._visible = value
    
    def draw(self, screen: pygame.Surface):
        """
        Render the text surface onto the given screen.
        
        Args:
            screen: The pygame surface to render onto
        """
        if not self._visible:
            return
        
        # Create the surface
        surface = pygame.Surface((self._width, self._height), pygame.SRCALPHA)
        
        # Fill background with color and opacity
        bg_color = (*self._background_color, self._opacity)
        surface.fill(bg_color)
        
        # Draw border if thickness > 0
        if self._border_thickness > 0:
            border_color = (*self._border_color, self._border_opacity)
            border_surface = pygame.Surface((self._width, self._height), pygame.SRCALPHA)
            pygame.draw.rect(border_surface, border_color, 
                           (0, 0, self._width, self._height), self._border_thickness)
            surface.blit(border_surface, (0, 0))
        
        # Render text if content exists
        if self._text_content and self._font:
            text_surface = self._font.render(self._text_content, True, self._text_color)
            text_rect = text_surface.get_rect()
            
            # Calculate text position based on alignment and padding
            content_width = self._width - self._padding_left - self._padding_right
            content_height = self._height - self._padding_top - self._padding_bottom
            
            # Horizontal alignment
            if self._horizontal_alignment == "left":
                text_x = self._padding_left
            elif self._horizontal_alignment == "center":
                text_x = self._padding_left + (content_width - text_rect.width) // 2
            else:  # right
                text_x = self._width - self._padding_right - text_rect.width
            
            # Vertical centering within padding
            text_y = self._padding_top + (content_height - text_rect.height) // 2
            
            # Ensure text stays within bounds
            text_x = max(self._padding_left, min(text_x, self._width - self._padding_right - text_rect.width))
            text_y = max(self._padding_top, min(text_y, self._height - self._padding_bottom - text_rect.height))
            
            surface.blit(text_surface, (text_x, text_y))
        
        # Blit to screen
        screen.blit(surface, (self._x_position, self._y_position))
    
    def set_position(self, x: int, y: int):
        """Convenience method to set both x and y position at once."""
        self._x_position = x
        self._y_position = y
    
    def set_size(self, width: int, height: int):
        """Convenience method to set both width and height at once."""
        self._width = max(0, width)
        self._height = max(0, height)
    
    def set_padding(self, top: int, right: int, bottom: int, left: int):
        """Convenience method to set all padding values at once."""
        self._padding_top = max(0, top)
        self._padding_right = max(0, right)
        self._padding_bottom = max(0, bottom)
        self._padding_left = max(0, left)
