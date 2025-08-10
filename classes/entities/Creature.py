import pygame
import os

from classes.effects.Animations import Animations

class Creature:
  def __init__(self, spritePath, animationSpeed, width = 50, height = 50, x = 0, y = 0):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.direction = "down"
    self.animationPhase = 0
    self.frameCounter = 0

    self.animations = Animations(spritePath, animationSpeed, width, height)

    self.sprites = self.load_sprites(spritePath)
    self.image = pygame.image.load(self.sprites['Down'][0])
    self.image = pygame.transform.scale(self.image, (self.width, self.height))

  def load_sprites(self, root_dir):
    directions = ["Up", "Down", "Left", "Right"]
    sprites = {}
    for direction in directions:
      dir_path = os.path.join(root_dir, direction)
      if os.path.isdir(dir_path):
        files = sorted([
          os.path.join(dir_path, f)
          for f in os.listdir(dir_path)
          if os.path.isfile(os.path.join(dir_path, f))
        ])
        sprites[direction] = files
      else:
        sprites[direction] = []
    return sprites

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))