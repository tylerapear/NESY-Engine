from classes.entities.Hitbox import Hitbox
import pygame

class Tile():
  
  def __init__(self, background_img_path, foreground_img_path = ""):
    self._background_img_path = background_img_path
    self._background_image = pygame.image.load(background_img_path)
    self._foreground_img_path = foreground_img_path
    self._foreground_image = None
    if foreground_img_path:
      self._foreground_image = pygame.image.load(foreground_img_path)
    
  def draw_background(self, screen, surface, x, y):
    scaled_background_image = pygame.transform.scale(
      self._background_image, (screen._tile_width, screen._tile_height)
    )
    surface.blit(scaled_background_image, (x, y))
    
  def draw_foreground(self, screen, surface, x, y):
    if self._foreground_image:
      scaled_foreground_image = pygame.transform.scale(
        self._foreground_image, (screen._tile_width, screen._tile_height + 40)
      )
      surface.blit(scaled_foreground_image, (x, y - 40))
    
    