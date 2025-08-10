import pygame

from classes.effects.Animations import Animations

class Creature:
  def __init__(self, spritePath, animationSpeed, width = 50, height = 50, x = 0, y = 0):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.direction = "Down"
    self.animationPhase = 0
    self.frameCounter = 0

    self.animations = Animations(spritePath, animationSpeed, width, height)

    self.image = self.animations.getNextImage("Idle")

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))

  def moveDirection(self, dt, direction, speed):
    if direction == "Up":
      self.y -= speed * dt
      if not self.direction == direction:
        self.image = self.animations.getNextImage(direction, True)
        self.direction = direction
      else:
        self.image = self.animations.getNextImage(direction)
    elif direction == "Down":
      self.y += speed * dt
      if not self.direction == direction:
        self.image = self.animations.getNextImage(direction, True)
        self.direction = direction
      else:
        self.image = self.animations.getNextImage(direction)
    elif direction == "Left":
      self.x -= speed * dt
      if not self.direction == direction:
        self.image = self.animations.getNextImage(direction, True)
        self.direction = direction
      else:
        self.image = self.animations.getNextImage(direction)
    elif direction == "Right":
      self.x += speed * dt
      if not self.direction == direction:
        self.image = self.animations.getNextImage(direction, True)
        self.direction = direction
      else:
        self.image = self.animations.getNextImage(direction)
