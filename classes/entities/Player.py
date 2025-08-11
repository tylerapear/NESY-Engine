import pygame
from classes.entities.Creature import Creature

class Player(Creature):

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
    hitbox_visible = False
  ):
    super().__init__(
      spritePath, 
      animationSpeed, 
      width, 
      height, 
      x, 
      y, 
      hitbox_width, 
      hitbox_height, 
      hitbox_x, 
      hitbox_y,
      hitbox_visible
    )
    self.attacking = False
    self.attack_cooldown = 0

  def attack(self, direction):
    if self.attack_cooldown <= 0:
      self.attack_cooldown = 20
      self.attacking = True
      self.image = self.animations.getNextImage("Attack" + direction, True)

  def checkForDamage(self, enemies):
    for enemy in enemies:
      if self.hitbox.collides(enemy.hitbox):
        pass

  def update(self, dt, enemies):

    self.checkForDamage(enemies)

    if self.attacking:
      self.frame_count += 1
      if self.frame_count >= 10:
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

    if self.attack_cooldown > 0:
      self.attack_cooldown -= 1
