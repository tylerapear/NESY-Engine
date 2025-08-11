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
    hitbox_visible = False,
    alive = True,
    health = 100,
    inventory = []
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
      hitbox_visible,
      alive,
      health
    )
    self.attacking = False
    self.attack_cooldown = 0
    self.inventory = inventory

  def attack(self, direction, weapon):
    if self.attack_cooldown <= 0:
      self.attack_cooldown = 20
      self.attacking = True
      self.image = self.animations.getNextImage("Attack" + direction, True)
      weapon.active = True

  def checkForDamage(self, enemies):
    for enemy in enemies:
      if self.hitbox.collides(enemy.hitbox):
        self.takeDamage(100)
        self.image = self.animations.getNextImage(self.direction, False, True)
        if self.health <= 0:
          self.alive = False

  def checkForGameOver(self):
    if not self.alive:
      return True

  def moveDirection(self, dt, direction, speed):
    super().moveDirection(dt, direction, speed)
    for item in self.inventory:
      if direction == "Up":
        item.hitbox.y -= speed * dt
      elif direction == "Down":
        item.hitbox.y += speed * dt
      elif direction == "Left":
        item.hitbox.x -= speed * dt
      elif direction == "Right":
        item.hitbox.x += speed * dt

  def update(self, dt, surface, enemies, weapon):

    self.checkForDamage(enemies)

    if self.attacking:
      self.frame_count += 1
      if self.frame_count >= 10:
        self.frame_count = 0
        self.attacking = False
        self.image = self.animations.getNextImage(self.direction, True)
        weapon.active = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_j]:
      self.attack(self.direction, weapon)

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

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))
    for item in self.inventory:
      item.drawHitbox(surface)
