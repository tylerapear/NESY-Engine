import pygame

class Player:
  
  def __init__(self, spritePath, width = 50, height = 50, x = 0, y = 0):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.image = pygame.image.load(spritePath)
    self.image = pygame.transform.scale(self.image, (self.width, self.height))

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))