from classes.entities.Hitbox import Hitbox
import pygame

class Tile():
  
  def __init__(self, width, height, img_path):
    self._width = width
    self._height = height
    self._img_path = img_path
    self._image = pygame.image.load(img_path)
    
    