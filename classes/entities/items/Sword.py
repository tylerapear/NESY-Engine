import pygame

from classes.entities.Hitbox import Hitbox

class Sword:
  def __init__(self, hitbox_width, hitbox_height, hitbox_x, hitbox_y, hitbox_visible = False):
    self.hitbox = Hitbox(hitbox_x, hitbox_y, hitbox_width, hitbox_height, hitbox_visible)
    self.active = False

  def drawHitbox(self, surface):
    if self.hitbox.visible and self.active:
      self.hitbox.draw(surface)
    