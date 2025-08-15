import pygame

from classes.entities.items.Item import Item
from classes.entities.Hitbox import Hitbox


class Sword(Item):
  def __init__(
    self,
    player,
    hitbox_visible = False, 
    damage = 100
  ):
    super().__init__()
    self.hitbox_down = {}
    self.hitbox_up = {}
    self.hitbox_left = {}
    self.hitbox_right = {}
    self.hitbox = Hitbox({"x": 0, "y": 0, "width": 0, "height": 0}, hitbox_visible)
    self.moveHitbox(player)
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

  def moveHitbox(self, player):
    self.hitbox_down = {"x": player.x + 110, "y": player.y + 160, "width": 18, "height": 60}
    self.hitbox_up = {"x": player.x + 109, "y": player.y + 14, "width": 18, "height": 65}
    self.hitbox_left = {"x": player.x + 15, "y": player.y + 115, "width": 65, "height": 18}
    self.hitbox_right = {"x": player.x + 170, "y": player.y + 115, "width": 65, "height": 18}
    if player.direction == "Down":
      self.setHitbox(self.hitbox_down)
    elif player.direction == "Up":
      self.setHitbox(self.hitbox_up)
    elif player.direction == "Left":
      self.setHitbox(self.hitbox_left)
    elif player.direction == "Right":
      self.setHitbox(self.hitbox_right)