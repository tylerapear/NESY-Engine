import pygame

class LogicalSurface():
  def __init__(self, width, height, background_color):
    self._surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    self._width = width
    self._height = height
    self._background_color = background_color
    
  # PROPERTIES #
  
  @property
  def surface(self):
    return self._surface
  
  @property
  def width(self):
    return self._width
  
  @property
  def height(self):
    return self._height
  
  @property
  def background_color(self):
    return self._background_color
  
  # METHODS #
    
  def compute_fit(self, dst_w, dst_h): 
    scale = min(dst_w / self.width, dst_h / self.height) 
    render_w, render_h = int(self.width * scale), int(self.height * scale) 
    x_off = (dst_w - render_w) // 2 
    y_off = (dst_h - render_h) // 2 
    return scale, x_off, y_off, render_w, render_h 
    
  def blit(self, surface):
    dst_w, dst_h = surface.get_size() 
    scale, x_off, y_off, render_w, render_h = self.compute_fit(dst_w, dst_h) 
    
    surface.fill(self.background_color) 
    
    if render_w == self.width and render_h == self.height: 
      surface.blit(self.surface, (x_off, y_off)) 
    else: 
      scaled = pygame.transform.smoothscale(self.surface, (render_w, render_h)) 
      surface.blit(scaled, (x_off, y_off)) 
    