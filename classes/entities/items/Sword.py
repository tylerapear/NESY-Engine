import pygame

from classes.entities.items.Item import Item
from classes.entities.Hitbox import Hitbox

# hitbox_width, hitbox_height, hitbox_x, hitbox_y

class Sword(Item):
  def __init__(
    self, 
    hitbox_dimentions_down,
    hitbox_dimentions_up,
    hitbox_dimentions_left,
    hitbox_dimentions_right, 
    hitbox_visible = False, 
    damage = 100
  ):
    super().__init__()
    self.hitbox = Hitbox(hitbox_dimentions_down, hitbox_visible)
    self.hitbox_down = hitbox_dimentions_down
    self.hitbox_up = hitbox_dimentions_up
    self.hitbox_left = hitbox_dimentions_left
    self.hitbox_right = hitbox_dimentions_right
    self.hitboxes = [self.hitbox_down, self.hitbox_up, self.hitbox_left, self.hitbox_right]
    self.damage = 10
    self.type = "Sword"

  def update(self, player):
    super().update(player)

  def drawHitbox(self, surface):
    if self.hitbox.visible and self.active:
      self.hitbox.draw(surface)

  def setHitbox(self, dimentions):
    self.hitbox.setX(dimentions["x"])
    self.hitbox.setY(dimentions["y"])
    self.hitbox.setWidth(dimentions["width"])
    self.hitbox.setHeight(dimentions["height"])

  def changeDirection(self, direction):
    if direction == "Up":
      self.setHitbox(self.hitbox_up)
    elif direction == "Down":
      self.setHitbox(self.hitbox_down)
    elif direction == "Left":
      self.setHitbox(self.hitbox_left)
    elif direction == "Right":
      self.setHitbox(self.hitbox_right)

  def moveHitbox(self, dt, speed, direction):
    if direction == "Up":
      print(f'Moving sword up {speed * dt}')
      for hitbox in self.hitboxes:
        hitbox["y"] -= speed * dt
      self.setHitbox(self.hitbox_up)
      #self.hitbox.setY(self.hitbox.getY() - (speed * dt))
    elif direction == "Down":
      for hitbox in self.hitboxes:
        hitbox["y"] += speed * dt
      self.setHitbox(self.hitbox_down)
      #self.hitbox.setY(self.hitbox.getY() + (speed * dt))
    elif direction == "Left":
      for hitbox in self.hitboxes:
        hitbox["x"] -= speed * dt
      self.setHitbox(self.hitbox_left)
      #self.hitbox.setX(self.hitbox.getX() - (speed * dt))
    elif direction == "Right":
      for hitbox in self.hitboxes:
        hitbox["x"] += speed * dt
      self.setHitbox(self.hitbox_right)
      #self.hitbox.setX(self.hitbox.getX() + (speed * dt))
    