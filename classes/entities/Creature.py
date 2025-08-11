import pygame

from classes.effects.Animations import Animations
from classes.entities.Hitbox import Hitbox

class Creature:
  def __init__(
    self, 
    spritePath, 
    animationSpeed, 
    width = 50, 
    height = 50, 
    x = 0, 
    y = 0, 
    hitbox_width = 50,
    hitbox_height = 50,
    hitbox_x = 0,
    hitbox_y = 0,
    hitbox_visible = False,
    alive = True,
    health = 100
  ):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.direction = "Down"
    self.animationPhase = 0
    self.frame_count = 0

    self.animations = Animations(spritePath, animationSpeed, width, height)
    self.image = self.animations.getNextImage("Idle")

    self.hitbox = Hitbox(hitbox_x, hitbox_y, hitbox_width, hitbox_height, hitbox_visible)

    self.alive = alive
    self.health = health

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))

    #TODO: REMOVE LINE
    self.hitbox.draw(surface) 

  def update(self, dt):
    pass

  def moveDirection(self, dt, direction, speed):
    if direction == "Up":
      self.y -= speed * dt
      self.hitbox.setY(self.hitbox.getY() - (speed * dt))
      if not self.direction == direction:
        self.image = self.animations.getNextImage(direction, True)
        self.direction = direction
      else:
        self.image = self.animations.getNextImage(direction)
    elif direction == "Down":
      self.y += speed * dt
      self.hitbox.setY(self.hitbox.getY() + (speed * dt))
      if not self.direction == direction:
        self.image = self.animations.getNextImage(direction, True)
        self.direction = direction
      else:
        self.image = self.animations.getNextImage(direction)
    elif direction == "Left":
      self.x -= speed * dt
      self.hitbox.setX(self.hitbox.getX() - (speed * dt))
      if not self.direction == direction:
        self.image = self.animations.getNextImage(direction, True)
        self.direction = direction
      else:
        self.image = self.animations.getNextImage(direction)
    elif direction == "Right":
      self.x += speed * dt
      self.hitbox.setX(self.hitbox.getX() + (speed * dt))
      if not self.direction == direction:
        self.image = self.animations.getNextImage(direction, True)
        self.direction = direction
      else:
        self.image = self.animations.getNextImage(direction)

  def takeDamage(self, damage):
    if self.health > 0:
      self.health -= damage