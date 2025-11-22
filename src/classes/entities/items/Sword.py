import pygame

from src.classes.entities.items.Item import Item
from src.classes.entities.Hitbox import Hitbox


class Sword(Item):
  def __init__(
    self,
    player,
    hitbox_visible = False, 
    damage = 100
  ):
    super().__init__()
    self._item_type = "Sword"
    self._damage = 10
    self._hitbox_down = {}
    self._hitbox_up = {}
    self._hitbox_left = {}
    self._hitbox_right = {}
    self._hitbox = Hitbox({"x": 0, "y": 0, "width": 0, "height": 0}, hitbox_visible)

    self.moveHitbox(player)

### PROPERTIES ###

  @property
  def item_type(self):
    return self._item_type

  @item_type.setter
  def item_type(self, item_type):
    self._item_type = item_type

  @property
  def damage(self):
    return self._damage

  @damage.setter
  def damage(self, damage):
    self._damage = damage

  @property
  def hitbox_down(self):
    return self._hitbox_down

  @hitbox_down.setter
  def hitbox_down(self, hitbox_down):
    self._hitbox_down = hitbox_down

  @property
  def hitbox_up(self):
    return self._hitbox_up

  @hitbox_up.setter
  def hitbox_up(self, hitbox_up):
    self._hitbox_up = hitbox_up

  @property
  def hitbox_left(self):
    return self._hitbox_left

  @hitbox_left.setter
  def hitbox_left(self, hitbox_left):
    self._hitbox_left = hitbox_left

  @property
  def hitbox_right(self):
    return self._hitbox_right

  @hitbox_right.setter
  def hitbox_right(self, hitbox_right):
    self._hitbox_right = hitbox_right

  @property
  def hitbox(self):
    return self._hitbox

### METHODS ###

  def update(self, player):
    super().update(player)

  def drawHitbox(self, surface):
    if self.hitbox.visible and self.active:
      self.hitbox.draw(surface)

  def setHitbox(self, dimentions):
    self.hitbox.x = dimentions["x"]
    self.hitbox.y = dimentions["y"]
    self.hitbox.width = dimentions["width"]
    self.hitbox.height = dimentions["height"]

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