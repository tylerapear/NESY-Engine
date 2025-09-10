from classes.entities.Hitbox import Hitbox
import pygame

class Tile():
  
  def __init__(self, background_img_path, foreground_img_path = ""):
    self._background_img_path = background_img_path
    self._foreground_img_path = foreground_img_path
    self._background_image = pygame.image.load(background_img_path)
    
    
    