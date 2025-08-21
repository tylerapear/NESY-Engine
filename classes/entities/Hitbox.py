import pygame

# x, y, width, height

class Hitbox:
  def __init__(self, hitbox_dimentions, visible = False):
    self._x = hitbox_dimentions["x"]
    self._y = hitbox_dimentions["y"]
    self._width = hitbox_dimentions["width"]
    self._height = hitbox_dimentions["height"]
    self._visible = visible

### PROPERTIES ###

  @property
  def x(self):
    return self._x

  @x.setter
  def x(self, x):
    self._x = x

  @property
  def y(self):
    return self._y

  @y.setter
  def y(self, y):
    self._y = y

  @property
  def width(self):
    return self._width

  @width.setter
  def width(self, width):
    self._width = width

  @property
  def height(self):
    return self._height

  @height.setter
  def height(self, height):
    self._height = height

  @property
  def visible(self):
    return self._visible

  @visible.setter
  def visible(self, visible):
    self._visible = visible

### METHODS ###

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
      self.x < hitbox.x + hitbox.width and #LEFT SIDE OF HITBOX
      self.x + self.width > hitbox.x and #RIGHT SIDE OF HITBOX
      self.y < hitbox.y + hitbox.height and #BOTTOM SIDE OF HITBOX
      self.y + self.height > hitbox.y
    ):
      return True

  def getCollisionDirection(self, hitbox):
    dY = self.y - hitbox.y
    dX = self.x - hitbox.x
    if self.y < ((hitbox.y - self.height) + 10):
      return "Up"
    elif (self.y - hitbox.height) > (hitbox.y - 10):
      return "Down"
    elif self.x < ((hitbox.x - self.width) + 10):
      return "Left"
    elif (self.x - hitbox.width) > (hitbox.x - 10):
      return "Right"
