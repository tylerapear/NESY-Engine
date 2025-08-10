import pygame

class Player:
  
  def __init__(self, width = 50, height = 50, x = 0, y = 0):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def draw(self, surface):
    pygame.draw.rect(surface, (255,255,255), (self.x, self.y, self.width, self.height))