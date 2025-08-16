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
    hitbox_dimentions = {"x": 0, "y": 0, "width": 0, "height": 0},
    hitbox_visible = False,
    alive = True,
    health = 100,
    display_health = True
  ):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.direction = "Down"
    self.moving = False
    self.animationPhase = 0
    self.frame_count = 0
    self.immunity_count = 0

    self.animations = Animations(spritePath, animationSpeed, width, height)
    self.current_animation = "IdleDown"

    self.hitbox = Hitbox(hitbox_dimentions, hitbox_visible)

    self.alive = alive
    self.health = health
    self.display_health = display_health
    self.damage_direction = "Down"

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))

    #TODO: REMOVE LINE
    self.hitbox.draw(surface) 

  def update(self, dt):
    if self.immunity_count > 0:
      self.immunity_count -= 1
      if self.immunity_count > 23:
        self.getKnockedBack(dt, self.damage_direction, 1000)
    
    self.image = self.animations.getNextImage(self, self.immunity_count)

  def draw(self, surface):
    if self.display_health:
      pygame.init()
      font = pygame.font.Font(None, 24)
      text_surface = font.render(str(self.health), True, (255,255,255))
      surface.blit(text_surface, (self.hitbox.getX() - 20, self.hitbox.getY() - 20))

    if self.hitbox.visible:
      self.hitbox.draw(surface) 

  def moveDirection(self, dt, direction, speed):
    self.moving = True
    self.direction = direction
    if self.immunity_count < 18:
      if direction == "Up":
        self.y -= speed * dt
        self.hitbox.setY(self.hitbox.getY() - (speed * dt))
      elif direction == "Down":
        self.y += speed * dt
        self.hitbox.setY(self.hitbox.getY() + (speed * dt))
      elif direction == "Left":
        self.x -= speed * dt
        self.hitbox.setX(self.hitbox.getX() - (speed * dt))
      elif direction == "Right":
        self.x += speed * dt
        self.hitbox.setX(self.hitbox.getX() + (speed * dt))

  def getKnockedBack(self, dt, direction, speed):
    if direction == "Up":
      self.y -= speed * dt
      self.hitbox.setY(self.hitbox.getY() - (speed * dt))
    elif direction == "Down":
      self.y += speed * dt
      self.hitbox.setY(self.hitbox.getY() + (speed * dt))
    elif direction == "Left":
      self.x -= speed * dt
      self.hitbox.setX(self.hitbox.getX() - (speed * dt))
    elif direction == "Right":
      self.x += speed * dt
      self.hitbox.setX(self.hitbox.getX() + (speed * dt))

  def takeDamage(self, damage):
    if self.health > 0:
      self.health -= damage
    self.immunity_count = 30