import pygame
from classes.effects.TextSurface import TextSurface

# Toggle to show/hide the text overlay globally
SHOW_TEXT_OVERLAY = False

def _render_text_to_surface(text, font_name, font_size, bold, color, max_width):
  size = max(8, int(font_size))
  while size >= 8:
    font = pygame.font.SysFont(font_name, size, bold=bold)
    surf = font.render(text, True, color)
    if surf.get_width() <= max_width or max_width <= 0:
      return surf, size
    size -= 2
  font = pygame.font.SysFont(font_name, 8, bold=bold)
  return font.render(text, True, color), 8

def drawTextSurface(dest_surface, textSurface):
  # Early exit if overlay is disabled
  if not SHOW_TEXT_OVERLAY:
    return

  # Defensive getters with defaults
  x = int(getattr(textSurface, "x_position", 0))
  y = int(getattr(textSurface, "y_position", 0))
  w = max(1, int(getattr(textSurface, "width", 400)))
  h = max(1, int(getattr(textSurface, "height", 100)))

  bg = tuple(getattr(textSurface, "background_color", (0, 0, 0)))
  opacity = int(getattr(textSurface, "opacity", 200))
  opacity = max(0, min(255, opacity))

  text = str(getattr(textSurface, "text_content", ""))
  color = tuple(getattr(textSurface, "text_color", (255, 255, 255)))
  font_size = int(getattr(textSurface, "font_size", 24))
  font_weight = str(getattr(textSurface, "font_weight", "normal")).lower()
  font_name = getattr(textSurface, "font_name", None)

  align = str(getattr(textSurface, "horizontal_alignment", "left")).lower()
  if align not in ("left", "center", "right"):
    align = "left"

  # Create a transparent panel surface
  panel = pygame.Surface((w, h), pygame.SRCALPHA)
  panel.fill((*bg, opacity))

  # Render text, auto-fit width with small margins
  side_margin = 10
  max_text_width = max(0, w - 2 * side_margin)
  bold = font_weight == "bold"
  text_surf, _ = _render_text_to_surface(
    text=text,
    font_name=font_name,
    font_size=font_size,
    bold=bold,
    color=color,
    max_width=max_text_width
  )

  text_rect = text_surf.get_rect()
  # Horizontal alignment inside panel
  if align == "left":
    text_rect.left = side_margin
  elif align == "center":
    text_rect.centerx = w // 2
  elif align == "right":
    text_rect.right = w - side_margin

  # Vertically center the text
  text_rect.centery = h // 2

  # Blit text onto the panel, then panel onto destination
  panel.blit(text_surf, text_rect)
  dest_surface.blit(panel, (x, y))

# Default textSurface instance (kept for future use; overlay disabled by default)
textSurface = TextSurface()
textSurface.text_content = "YOU BUFFOON!"
textSurface.background_color = (15, 15, 15)
textSurface.x_position = 20
textSurface.y_position = 300
textSurface.width = 1240
textSurface.height = 200
textSurface.opacity = 230
textSurface.text_color = (255, 255, 255)
textSurface.font_size = 128
textSurface.horizontal_alignment = "center"
textSurface.font_weight = "bold"
