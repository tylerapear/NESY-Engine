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
    hitbox_dimentions = {"x": 0, "y": 0, "width": 0, "height": 0},
    hitbox_visible = False,
    alive = True,
    health = 100,
    display_health = True,
    inventory = []
  ):
    super().__init__(
      spritePath, 
      animationSpeed, 
      width, 
      height, 
      x, 
      y, 
      hitbox_dimentions,
      hitbox_visible,
      alive,
      health,
      display_health
    )
    self._attacking = False
    self._attack_cooldown = 0
    self._inventory = inventory

### PROPERTIES ###

  @property
  def attacking(self):
    return self._attacking

  @attacking.setter
  def attacking(self, attacking):
    self._attacking = attacking

  @property
  def attack_cooldown(self):
    return self._attack_cooldown

  @attack_cooldown.setter
  def attack_cooldown(self, attack_cooldown):
    self._attack_cooldown = attack_cooldown

  @property
  def inventory(self):
    return self._inventory

  @inventory.setter
  def inventory(self, inventory):
    self._inventory = inventory

### METHODS ###

  def update(self, dt, surface, enemies, weapon):
    super().update(dt)

    ### UPDATE INVENTORY ITEMS ###
    for item in self.inventory:
      item.update(self)

    ### CHECK FOR DAMAGE ###
    self.checkForDamage(enemies)

    ### HANDLE ATTACKING ###
    if self.attacking:
      self.frame_count += 1
      if self.frame_count >= 10:
        self.frame_count = 0
        self.attacking = False
        weapon.active = False

    if self.attack_cooldown > 0:
      self.attack_cooldown -= 1
      if self.attack_cooldown < 5:
        self.attacking = False
        self.current_animation = self.direction

    ### HANDLE MOVEMENT ###
    keys = pygame.key.get_pressed()

    if keys[pygame.K_j]:
      self.attack(self.direction, weapon)

    self.moving = False
    if not self.attacking:
      if keys[pygame.K_s]:
        self.moveDirection(dt, "Down", 200)
      elif keys[pygame.K_w]:
        self.moveDirection(dt, "Up", 200)
      elif keys[pygame.K_a]:
        self.moveDirection(dt, "Left", 200)
      elif keys[pygame.K_d]:
        self.moveDirection(dt, "Right", 200)

    ### Update Animation ###
    self.current_animation = "Idle" + self.direction
    if self.moving:
      self.current_animation = self.direction
    if self.attacking:
      self.current_animation = "Attack" + self.direction

  def draw(self, surface):
    super().draw(surface)
    surface.blit(self.image, (self.x, self.y))
    for item in self.inventory:
      item.drawHitbox(surface)

  def attack(self, direction, weapon):
    if self.attack_cooldown <= 0:
      self.attack_cooldown = 15
      self.attacking = True
      self.current_animation = "Attack" + direction
      weapon.active = True

  def checkForDamage(self, enemies):
    for enemy in enemies:
      if self.hitbox.collides(enemy.hitbox) and self.immunity_count <= 0:
        self.damage_direction = self.hitbox.getCollisionDirection(enemy.hitbox)
        self.takeDamage(10)
        self.immunity_count = 30
        if self.health <= 0:
          self.alive = False

  def getKnockedBack(self, dt, direction, speed):
    super().getKnockedBack(dt, direction, speed)
    for item in self.inventory:
      item.moveHitbox(self)

  def checkForGameOver(self):
    if not self.alive:
      return True

  def moveDirection(self, dt, direction, speed):
    super().moveDirection(dt, direction, speed)
    for item in self.inventory:
      item.moveHitbox(self)


