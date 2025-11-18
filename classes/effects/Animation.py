import pygame
import os

class Animation:
  def __init__(self, spritePath, speed, width, height):
    self._spritePath = spritePath
    self._speed = speed
    self._width = width
    self._height = height
    self._phase = 0
    self._frame_count = 0
    self._images = self.load_images(spritePath)
    self._current_image_path = self._images[0]
    self._current_image = pygame.image.load(self._current_image_path)
    self._current_image = pygame.transform.scale(self._current_image, (self.width, self.height))

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
  def images(self):
    return self._images

  @images.setter
  def images(self, images):
    self._images = images

  @property
  def current_image(self):
    return self._current_image

  @current_image.setter
  def current_image(self, current_image):
    self._current_image = current_image

### METHODS ###

  def load_images(self, root_dir):

    files = sorted([
      os.path.join(root_dir, f)
      for f in os.listdir(root_dir)
    ])

    return files

  def getNextImage(self, entity, immunity_count = 0): 
    if entity.current_animation != self.current_animation:
      self.phase = 0
      self.frame_count = self.speed - 1
      self.current_animation = entity.current_animation

    self.frame_count += 1

    if "Death" in self.current_animation:
        if self.frame_count >= self.speed:
            self.frame_count = 0
            self.image = pygame.image.load(self.animations[self.current_animation][self.phase])
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            if self.phase < len(self.animations[self.current_animation]) - 1:
                self.phase += 1
    else:
        if self.frame_count >= self.speed:
            self.frame_count = 0
            self.image = pygame.image.load(self.animations[self.current_animation][self.phase])
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            if self.phase >= len(self.animations[self.current_animation]) - 1:
                self.phase = 0
            else:
                self.phase += 1

    #flash red when taking damage
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
  
  def update(self):
    # set current image
    self.current_image_path = self._images[0]
    self.current_image = pygame.image.load(self.current_image_path)
    self.current_image = pygame.transform.scale(self.current_image, (self.width, self.height))