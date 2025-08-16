import pygame

# x, y, width, height

class Hitbox:
  def __init__(self, hitbox_dimentions, visible = False):
    self.x = hitbox_dimentions["x"]
    self.y = hitbox_dimentions["y"]
    self.width = hitbox_dimentions["width"]
    self.height = hitbox_dimentions["height"]
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
      return True

  def getCollisionDirection(self, hitbox):
    dY = self.y - hitbox.getY()
    dX = self.x - hitbox.getX()
    if self.y < ((hitbox.getY() - self.height) + 10):
      return "Up"
    elif (self.y - hitbox.getHeight()) > (hitbox.getY() - 10):
      return "Down"
    elif self.x < ((hitbox.getX() - self.width) + 10):
      return "Left"
    elif (self.x - hitbox.getWidth()) > (hitbox.getX() - 10):
      return "Right"

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
