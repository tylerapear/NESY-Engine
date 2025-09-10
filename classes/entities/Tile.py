from classes.entities.Hitbox import Hitbox
import pygame

class Tile():
  
  def __init__(
      self, 
      background_img_path, 
      foreground_img_path = "", 
      hitbox_active = False, 
      hitbox_dimentions = {"x": 0, "y": 0, "width": 0, "height": 0},
      hitbox_offset = {"x": 0, "y": 0, "width": 0, "height": 0},
      hitbox_visible = False
    ):
    self._background_img_path = background_img_path
    self._background_image = pygame.image.load(background_img_path)
    self._foreground_img_path = foreground_img_path
    self._foreground_image = None
    if foreground_img_path:
      self._foreground_image = pygame.image.load(foreground_img_path)
    self._hitbox_active = hitbox_active
    self._hitbox = Hitbox(hitbox_dimentions, hitbox_visible)
    self._hitbox.offset = hitbox_offset
    
  def draw_background(self, screen, surface, x, y):
    scaled_background_image = pygame.transform.scale(
      self._background_image, (screen._tile_width, screen._tile_height)
    )
    surface.blit(scaled_background_image, (x, y))
    
  def draw_foreground(self, screen, surface, x, y):
    if self._foreground_image:
      scaled_foreground_image = pygame.transform.scale(
        self._foreground_image, (screen._tile_width, screen._tile_height + 15)
      )
      surface.blit(scaled_foreground_image, (x, y - 15))

    self._hitbox.x = x + screen._tile_width * self._hitbox.offset["x"]
    self._hitbox.y = y + (screen._tile_height * self._hitbox.offset["y"]) - 15
    self._hitbox.width = screen._tile_width * self._hitbox.offset["width"]
    self._hitbox.height = (screen._tile_height + 15) * self._hitbox.offset["height"]
    self._hitbox.draw(surface)

    
    