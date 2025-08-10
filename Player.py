import pygame
import os

class Player:
  
  def __init__(self, spritePath, width = 50, height = 50, x = 0, y = 0):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.direction = "down"
    self.animationPhase = 0
    self.frameCounter = 0

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
    print(sprites)
    return sprites

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))

  def moveUp(self, dt, speed):
    self.y -= speed * dt
    if not self.direction == "up":
       self.animationPhase = 0
       self.direction = "up"
       self.frameCounter = 9
    self.frameCounter += 1
    if self.frameCounter >= 10:
      self.frameCounter = 0
      self.image = pygame.image.load(self.sprites['Up'][self.animationPhase])
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
      print(f"Len: {len(self.sprites['Up']) - 1}")
      if self.animationPhase >= len(self.sprites['Up']) - 1:
        self.animationPhase = 0
      else:
        self.animationPhase += 1
      print(self.animationPhase)

  def moveDown(self, dt, speed):
    self.y += speed * dt
    if not self.direction == "down":
       self.animationPhase = 0
       self.direction = "down"
       self.frameCounter = 9
    self.frameCounter += 1
    if self.frameCounter >= 10:
      self.frameCounter = 0
      self.image = pygame.image.load(self.sprites['Down'][self.animationPhase])
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
      print(f"Len: {len(self.sprites['Down']) - 1}")
      if self.animationPhase >= len(self.sprites['Down']) - 1:
        self.animationPhase = 0
      else:
        self.animationPhase += 1
      print(self.animationPhase)

  def moveLeft(self, dt, speed):
    self.x -= speed * dt
    if not self.direction == "left":
       self.animationPhase = 0
       self.direction = "left"
       self.frameCounter = 9
    self.frameCounter += 1
    if self.frameCounter >= 10:
      self.frameCounter = 0
      self.image = pygame.image.load(self.sprites['Left'][self.animationPhase])
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
      print(f"Len: {len(self.sprites['Left']) - 1}")
      if self.animationPhase >= len(self.sprites['Left']) - 1:
        self.animationPhase = 0
      else:
        self.animationPhase += 1
      print(self.animationPhase)

  def moveRight(self, dt, speed):
    self.x += speed * dt
    if not self.direction == "right":
       self.animationPhase = 0
       self.direction = "right"
       self.frameCounter = 9
    self.frameCounter += 1
    if self.frameCounter >= 10:
      self.frameCounter = 0
      self.image = pygame.image.load(self.sprites['Right'][self.animationPhase])
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
      print(f"Len: {len(self.sprites['Right']) - 1}")
      if self.animationPhase >= len(self.sprites['Right']) - 1:
        self.animationPhase = 0
      else:
        self.animationPhase += 1
      print(self.animationPhase)