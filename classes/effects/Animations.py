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
    self.current_animation = "Idle"
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


  def getNextImage(self, entity, immunity_count = 0):
    if entity.current_animation != self.current_animation:
      self.phase = 0
      self.frame_count = self.speed - 1
      self.current_animation = entity.current_animation

    self.frame_count += 1

    if self.frame_count >= self.speed:
      self.frame_count = 0
      self.image = pygame.image.load(self.animations[self.current_animation][self.phase])
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
      if self.phase >= len(self.animations[self.current_animation]) - 1:
          self.phase = 0
      else:
        self.phase += 1
      
    return self.image

  '''
  def getNextImage(self, animation, startOver = False, damageImage = False):
    if startOver:
      self.phase = 0
      self.frame_count = self.speed - 1

    self.frame_count += 1

    if damageImage:
      image = pygame.image.load(self.animations[animation][self.phase])
      red_image = image.copy()
      red_image.fill((255,0,0,255), special_flags=pygame.BLEND_RGBA_MULT)
      self.image = red_image

      self.image = pygame.transform.scale(self.image, (self.width, self.height))
    else:
      if self.frame_count >= self.speed:
        self.frame_count = 0
        self.image = pygame.image.load(self.animations[animation][self.phase])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if self.phase >= len(self.animations[animation]) - 1:
          self.phase = 0
        else:
          self.phase += 1
      
    return self.image
    '''