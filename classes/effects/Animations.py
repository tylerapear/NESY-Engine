import pygame
import os

class Animations:
  def __init__(self, spritePath, speed, width, height):
    self._spritePath = spritePath
    self._speed = speed
    self._width = width
    self._height = height
    self._phase = 0
    self._frame_count = 0
    self._animations = self.load_animations(spritePath)
    self._current_animation = "Idle"
    self._image = pygame.image.load(self.animations["Idle"][self.phase])
    self._image = pygame.transform.scale(self.image, (self.width, self.height))

### PROPERTIES ###

  @property
  def spritePath(self):
    return self._spritePath

  @spritePath.setter
  def spritePath(self, path):
    self._spritePath = path

  @property
  def speed(self):
    return self._speed

  @speed.setter
  def speed(self, speed):
    self._speed = speed

  @property
  def width(self):
    return self._width

  @width.setter
  def width(self, width):
    self._width = width

  @property
  def height(self):
    return self._height

  @height.setter
  def height(self, height):
    self._height = height

  @property
  def phase(self):
    return self._phase

  @phase.setter
  def phase(self, phase):
    self._phase = phase

  @property
  def animations(self):
    return self._animations

  @animations.setter
  def animations(self, animations):
    self._animations = animations

  @property
  def current_animation(self):
    return self._current_animation

  @current_animation.setter
  def current_animation(self, current_animation):
    self._current_animation = current_animation

  @property
  def image(self):
    return self._image

  @image.setter
  def image(self, image):
    self._image = image

### METHODS ###

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

    if immunity_count > 15:
      image = self.image
      damage_image = image.copy()
      damage_image.fill((0, 0, 0, 255), special_flags=pygame.BLEND_RGBA_MULT)
      if( 
        (immunity_count > 24 and immunity_count < 29) or 
        (immunity_count > 15 and immunity_count < 18)
      ):
        damage_image.fill((180,20,20,0), special_flags=pygame.BLEND_RGBA_ADD)
      else:
        damage_image.fill((255, 255, 255, 0), special_flags=pygame.BLEND_RGBA_ADD)
      self.image = damage_image
      
    return self.image