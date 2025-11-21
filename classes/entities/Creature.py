import pygame

#from classes.effects.Animations import Animations
from classes.effects.Animation import Animation
from classes.entities.Hitbox import Hitbox

class Creature:
  def __init__(
    self, 
    animationSpeed,
    animations,
    width = 50, 
    height = 50, 
    x = 0, 
    y = 0, 
    hitbox_offset_dimentions = {"x": 0, "y": 0, "width": 0, "height": 0},
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
    self._frame_count = 0
    self._immunity_count = 0

    self._animations = animations
    self._current_animation = Animation("./assets/Sprites/Default", 10, 250, 250)
    #self._current_animation = "IdleDown"
    #self._current_image = self._current_animation["path"]

    self._hitbox_offset_dimentions = hitbox_offset_dimentions
    self._hitbox = Hitbox(
      {
        "x": x + hitbox_offset_dimentions["x"], 
        "y": y + hitbox_offset_dimentions["y"], 
        "width": hitbox_offset_dimentions["width"], 
        "height": hitbox_offset_dimentions["height"]
      }, 
      hitbox_visible
    )

    self._alive = alive
    self._movement_locked = False
    self._dying = False
    self._health = health
    self.max_health = health
    self._display_health = display_health
    self._damage_direction = "Down"
    
    self._up_speed = 1
    self._down_speed = 1
    self._left_speed = 1
    self._right_speed = 1

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
    self._current_animation.phase = 0

  @property
  def hitbox_offset_dimentions(self):
    return self._hitbox_offset_dimentions

  @hitbox_offset_dimentions.setter
  def hitbox_offset_dimentions(self, hitbox_offset_dimentions, visible = False):
    self._hitbox_offset_dimentions = hitbox_offset_dimentions

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
  def movement_locked(self):
    return self._movement_locked

  @movement_locked.setter
  def movement_locked(self, movement_locked):
    self._movement_locked = movement_locked
    
  @property
  def dying(self):
    return self._dying

  @dying.setter
  def dying(self, dying):
    self._dying = dying

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
    
  @property
  def up_speed(self):
    return self._up_speed

  @up_speed.setter
  def up_speed(self, up_speed):
    self._up_speed = up_speed
    
  @property
  def down_speed(self):
    return self._down_speed

  @down_speed.setter
  def down_speed(self, down_speed):
    self._down_speed = down_speed
    
  @property
  def left_speed(self):
    return self._left_speed

  @left_speed.setter
  def left_speed(self, left_speed):
    self._left_speed = left_speed
    
  @property
  def right_speed(self):
    return self._right_speed

  @right_speed.setter
  def right_speed(self, right_speed):
    self._right_speed = right_speed

### METHODS ###

  def update(self, dt, FRAMERATE, world_map):

    if self.health <= 0:
      self.progress_death()
      #elif self.dying:
        #if "Death" in self.animations:
          #self.current_animation = self.animations["Death"]

    else:  
      self.up_speed = 1
      if self.hitbox.y <= 0:
        self.handleBorderCollision(world_map, "Up")
        
      self.left_speed = 1
      if self.hitbox.x <= 0:
        self.handleBorderCollision(world_map, "Left")
        
      self.down_speed = 1
      if self.hitbox.y + self.hitbox.height >= world_map.current_screen.height:
        self.handleBorderCollision(world_map, "Down")
        
      self.right_speed = 1
      if self.hitbox.x + self.hitbox.width >= world_map.current_screen.width:
        self.handleBorderCollision(world_map, "Right")

      for tile in world_map.current_screen.tiles:
        if tile.hitbox_active and self.hitbox.collides(tile.hitbox):
          collision_direction = self.hitbox.getReverseCollisionDirection(tile.hitbox)
          self.handleTileCollision(collision_direction)
      
      if self.immunity_count > 0:
        self.immunity_count -= 1
        if self.immunity_count > 23:
          self.getKnockedBack(dt, self.damage_direction, 1000)
      
    self.current_animation.update(FRAMERATE, self.immunity_count)
    if self.dying and self.current_animation == "Death":
      last_frame_index = len(self.animations.animations["Death"]) - 1
      if self.animations.phase == last_frame_index:
        #waiting a few ticks for the last frame
        self.alive = False

  def draw(self, surface):
    surface.blit(self.current_animation.current_image, (self.x, self.y))
    if self.display_health:
      pygame.init()
      font = pygame.font.Font(None, 24)
      text_surface = font.render(str(self.health), True, (255,255,255))
      surface.blit(text_surface, (self.hitbox.x - 20, self.hitbox.y - 20))

    if self.hitbox.visible:
      self.hitbox.draw(surface) 

  def moveDirection(self, dt, direction, speed):
    if not self.movement_locked:
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

  def moveTo(self, x, y):
    self.x = x
    self.hitbox.x = self.x + self.hitbox_offset_dimentions["x"]
    self.y = y
    self.hitbox.y = self.y + self.hitbox_offset_dimentions["y"]

  def getKnockedBack(self, dt, direction, speed):
    if direction == "Up":
      self.y -= speed * dt * self.up_speed
      self.hitbox.y = self.hitbox.y - ((speed * dt) * self.up_speed)
    elif direction == "Down":
      self.y += speed * dt * self.down_speed
      self.hitbox.y = self.hitbox.y + ((speed * dt) * self.down_speed)
    elif direction == "Left":
      self.x -= speed * dt * self.left_speed
      self.hitbox.x = self.hitbox.x - ((speed * dt) * self.left_speed)
    elif direction == "Right":
      self.x += speed * dt * self.right_speed
      self.hitbox.x = self.hitbox.x + ((speed * dt) * self.right_speed)

  def takeDamage(self, damage):
    self.health -= damage
    if self.health <= 0:
      self.health = 0 #avoid neg hp
    self.immunity_count = 30
    
  def handleBorderCollision(self, world_map, direction):
    if direction == "Up":
      self.up_speed = 0
    if direction == "Down":
      self.down_speed = 0
    if direction == "Left":
      self.left_speed = 0
    if direction == "Right":
      self.right_speed = 0
      
  def handleTileCollision(self, direction):
    if direction == "Up":
      self.up_speed = 0
    if direction == "Down":
      self.down_speed = 0
    if direction == "Left":
      self.left_speed = 0
    if direction == "Right":
      self.right_speed = 0

  def progress_death(self):
    print("progressing death")
    if not self.dying:
      self.dying = True
      self.movement_locked = True
      if "Death" in self.animations:
          self.current_animation = self.animations["Death"]
    elif self.current_animation.phase < len(self.current_animation.images) - 1:
        return
    else:
      self.alive = False
      