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
    dx_left = (self.x + self.width) - hitbox.x
    dx_right = self.x - (hitbox.x + hitbox.width)
    dy_top = (self.y + self.height) - hitbox.y
    dy_bottom = self.y - (hitbox.y + hitbox.height)
    
    min_dx = min(abs(dx_left), abs(dx_right))
    min_dy = min(abs(dy_top), abs(dy_bottom))
    
    if min_dx < min_dy:
        if dx_left > 0:
            return "Left"
        else:
            return "Right"
    else:
        if dy_top > 0:
            return "Up"
        else:
            return "Down"

  def getReverseCollisionDirection(self, hitbox):
    dx_left = abs((self.x + self.width) - hitbox.x)
    dx_right = abs(self.x - (hitbox.x + hitbox.width))
    dy_top = abs((self.y + self.height) - hitbox.y)
    dy_bottom = abs(self.y - (hitbox.y + hitbox.height))
    
    min_dx = min(dx_left, dx_right)
    min_dy = min(dy_top, dy_bottom)
    
    if min_dx < min_dy:
      if dx_left < dx_right:
        return "Right"
      else:
        return "Left"
    else:
      if dy_top < dy_bottom:
        return "Down"
      else:
        return "Up"
