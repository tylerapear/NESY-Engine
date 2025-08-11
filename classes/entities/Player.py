import pygame
from classes.entities.Creature import Creature

class Player(Creature):

  def __init__(self, spritePath, animationSpeed, width = 50, height = 50, x = 0, y = 0):
    super().__init__(spritePath, animationSpeed, width, height, x, y)
    self.attacking = False

  def attack(self, direction):
    self.attacking = True
    self.image = self.animations.getNextImage("Attack" + direction, True)

  def update(self, dt):

    if self.attacking:
      self.frame_count += 1
      if self.frame_count >= 20:
        self.frame_count = 0
        self.attacking = False
        self.image = self.animations.getNextImage(self.direction, True)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_j]:
      self.attack(self.direction)

    if self.attacking == False:
      if keys[pygame.K_s]:
        self.moveDirection(dt, "Down", 200)
      elif keys[pygame.K_w]:
        self.moveDirection(dt, "Up", 200)
      elif keys[pygame.K_a]:
        self.moveDirection(dt, "Left", 200)
      elif keys[pygame.K_d]:
        self.moveDirection(dt, "Right", 200)
