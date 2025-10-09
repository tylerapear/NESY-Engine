from classes.entities.Hitbox import Hitbox
import pygame

class Tile():
  
  def __init__(
      self, 
      background_img_path, 
      foreground_img_path = "", 
      hitbox_active = False, 
      #hitbox_dimentions = {"x": 0, "y": 0, "width": 0, "height": 0},
      hitbox_offset = {"x": 0, "y": 0, "width": 0, "height": 0},
      hitbox_visible = False
    ):
    self._background_img_path = background_img_path
    self._background_image = pygame.image.load(background_img_path)
    self._foreground_img_path = foreground_img_path
    self._foreground_image = None
    if foreground_img_path:
      self._foreground_image = pygame.image.load(foreground_img_path)
    self._hitbox_active = hitbox_active
    self._hitbox = Hitbox({"x": 0, "y": 0, "width": 0, "height": 0}, hitbox_visible) #Hitbox(hitbox_dimentions, hitbox_visible)
    self._hitbox.offset = hitbox_offset
    
### PROPERTIES ###

  @property
  def background_img_path(self):
    return self._background_img_path
  
  @background_img_path.setter
  def background_img_path(self, background_img_path):
    self._background_img_path = background_img_path
    
  @property
  def background_image(self):
    return self._background_image
  
  @background_image.setter
  def background_image(self, background_image):
    self._background_image = background_image
    
  @property
  def foreground_img_path(self):
    return self._foreground_img_path
  
  @foreground_img_path.setter
  def foreground_img_path(self, foreground_img_path):
    self._foreground_img_path = foreground_img_path
    
  @property
  def foreground_image(self):
    return self._foreground_image
  
  @foreground_image.setter
  def foreground_image(self, foreground_image):
    self._foreground_image = foreground_image
    
  @property
  def hitbox_active(self):
    return self._hitbox_active
  
  @hitbox_active.setter
  def hitbox_active(self, hitbox_active):
    self._hitbox_active = hitbox_active
    
  @property
  def hitbox(self):
    return self._hitbox
    
  @property
  def prop1(self):
    return self._prop1

### METHODS ### 
    
  def draw_background(self, screen, surface, x, y):
    scaled_background_image = pygame.transform.scale(
      self.background_image, (screen.tile_width, screen.tile_height)
    )
    print(scaled_background_image.get_size())
    surface.blit(scaled_background_image, (x, y))
    
  def draw_foreground(self, screen, surface, x, y):
    if self.foreground_image:
      scaled_foreground_image = pygame.transform.scale(
        self.foreground_image, (screen.tile_width, screen.tile_height + 0)
      )
      surface.blit(scaled_foreground_image, (x, y - 0))

    self.hitbox.x = x + screen.tile_width * self.hitbox.offset["x"]
    self.hitbox.y = y + (screen.tile_height * self.hitbox.offset["y"]) - 0
    self.hitbox.width = screen.tile_width * self.hitbox.offset["width"]
    self.hitbox.height = (screen.tile_height + 0) * self.hitbox.offset["height"]
    self.hitbox.draw(surface)

    
    