import pygame
import os

class Animations:
  def __init__(self, spritePath, speed, width, height):
    self.spritePath = spritePath
    self.speed = speed
    self.width = width
    self.height = height
    self.phase = 0
    self.frame_count = 0
    self.animations = self.load_animations(spritePath)
    self.image = pygame.image.load(self.animations["Idle"][self.phase])
    self.image = pygame.transform.scale(self.image, (self.width, self.height))

  def load_animations(self, root_dir):
    directions = ["Up", "Down", "Left", "Right"]
    animations = {}

    for folder in os.listdir(root_dir):
      dir_path = os.path.join(root_dir, folder)
      files = sorted([
        os.path.join(dir_path, f)
        for f in os.listdir(dir_path)
      ])
      animations[folder] = files

    return animations


  def getNextImage(self, animation, startOver = False):
    if startOver:
      self.phase = 0
      self.frame_count = self.speed - 1

    self.frame_count += 1

    if self.frame_count >= self.speed:
      self.frame_count = 0
      self.image = pygame.image.load(self.animations[animation][self.phase])
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
      if self.phase >= len(self.animations[animation]) - 1:
        self.phase = 0
      else:
        self.phase += 1
      
    return self.image