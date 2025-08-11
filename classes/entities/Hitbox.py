import pygame

class Hitbox:
  def __init__(self, x, y, width, height, visible = False):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.visible = visible

  def draw(self, surface, color=(255,0,0), border_width=1):
    if self.visible:
      pygame.draw.rect(
        surface,
        color,
        (self.x, self.y, self.width, self.height),
        border_width
      )

  def collides(self, hitbox):
    if (
      self.x < hitbox.getX() + hitbox.getWidth() and #LEFT SIDE OF HITBOX
      self.x + self.width > hitbox.getX() and #RIGHT SIDE OF HITBOX
      self.y < hitbox.getY() + hitbox.getHeight() and #BOTTOM SIDE OF HITBOX
      self.y + self.height > hitbox.getY()
    ):
      print("collide!")
    else:
      print("not collide")

  def setX(self, x):
    self.x = x

  def setY(self, y):
    self.y = y

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def setWidth(self, width):
    self.width = width

  def setHeight(self, height):
    self.height = height

  def getWidth(self):
    return self.width

  def getHeight(self):
    return self.height
