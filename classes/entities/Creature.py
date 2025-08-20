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
    self._x = x
    self._y = y
    self._width = width
    self._height = height
    self._direction = "Down"
    self._moving = False
    self._animationPhase = 0
    self._frame_count = 0
    self._immunity_count = 0

    self._animations = Animations(spritePath, animationSpeed, width, height)
    self._current_animation = "IdleDown"

    self._hitbox = Hitbox(hitbox_dimentions, hitbox_visible)

    self._alive = alive
    self._health = health
    self._display_health = display_health
    self._damage_direction = "Down"

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
  def direction(self):
    return self._direction

  @direction.setter
  def direction(self, direction):
    self._direction = direction

  @property
  def moving(self):
    return self._moving

  @moving.setter
  def moving(self, moving):
    self._moving = moving

  @property
  def animationPhase(self):
    return self._animationPhase

  @animationPhase.setter
  def animationPhase(self, animationPhase):
    self._animationPhase = animationPhase
  
  @property
  def frame_count(self):
    return self._frame_count

  @frame_count.setter
  def frame_count(self, frame_count):
    self._frame_count = frame_count

  @property
  def immunity_count(self):
    return self._immunity_count

  @immunity_count.setter
  def immunity_count(self, immunity_count):
    self._immunity_count = immunity_count

  @property
  def animations(self):
    return self._animations

  @animations.setter
  def animations(self, spritePath, animationSpeed, width, height):
    self._animations = Animations(spritePath, animationSpeed, width, height)

  @property
  def current_animation(self):
    return self._current_animation

  @current_animation.setter
  def current_animation(self, current_animation):
    self._current_animation = current_animation

  @property
  def hitbox(self):
    return self._hitbox

  @hitbox.setter
  def hitbox(self, hitbox_dimentions, visible = False):
    self._hitbox = Hitbox(hitbox_dimentions, visible)

  @property
  def alive(self):
    return self._alive

  @alive.setter
  def alive(self, alive):
    self._alive = alive

  @property
  def health(self):
    return self._health

  @health.setter
  def health(self, health):
    self._health = health

  @property
  def display_health(self):
    return self._display_health

  @display_health.setter
  def display_health(self, display_health):
    self._display_health = display_health

  @property
  def damage_direction(self):
    return self._damage_direction

  @damage_direction.setter
  def damage_direction(self, damage_direction):
    self._damage_direction = damage_direction

### METHODS ###

  def update(self, dt):
    if self.immunity_count > 0:
      self.immunity_count -= 1
      if self.immunity_count > 23:
        self.getKnockedBack(dt, self.damage_direction, 1000)
    
    self.image = self.animations.getNextImage(self, self.immunity_count)

  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))
    if self.display_health:
      pygame.init()
      font = pygame.font.Font(None, 24)
      text_surface = font.render(str(self.health), True, (255,255,255))
      surface.blit(text_surface, (self.hitbox.x - 20, self.hitbox.y - 20))

    if self.hitbox.visible:
      self.hitbox.draw(surface) 

  def moveDirection(self, dt, direction, speed):
    self.moving = True
    self.direction = direction
    if self.immunity_count < 18:
      if direction == "Up":
        self.y -= speed * dt
        self.hitbox.y = self.hitbox.y - (speed * dt)
      elif direction == "Down":
        self.y += speed * dt
        self.hitbox.y = self.hitbox.y + (speed * dt)
      elif direction == "Left":
        self.x -= speed * dt
        self.hitbox.x = self.hitbox.x - (speed * dt)
      elif direction == "Right":
        self.x += speed * dt
        self.hitbox.x = self.hitbox.x + (speed * dt)

  def getKnockedBack(self, dt, direction, speed):
    if direction == "Up":
      self.y -= speed * dt
      self.hitbox.y = self.hitbox.y - (speed * dt)
    elif direction == "Down":
      self.y += speed * dt
      self.hitbox.y = self.hitbox.y + (speed * dt)
    elif direction == "Left":
      self.x -= speed * dt
      self.hitbox.x = self.hitbox.x - (speed * dt)
    elif direction == "Right":
      self.x += speed * dt
      self.hitbox.x = self.hitbox.x + (speed * dt)

  def takeDamage(self, damage):
    if self.health > 0:
      self.health -= damage
    self.immunity_count = 30