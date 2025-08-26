import pygame

class LogicalSurface():
  def __init__(self, width, height, background_color):
    self.surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    self._width = width
    self._height = height
    self._background_color = background_color
    
  def compute_fit(self, dst_w, dst_h): 
    scale = min(dst_w / self._width, dst_h / self._height) 
    render_w, render_h = int(self._width * scale), int(self._height * scale) 
    x_off = (dst_w - render_w) // 2 
    y_off = (dst_h - render_h) // 2 
    return scale, x_off, y_off, render_w, render_h 
    
  def blit(self, surface):
    dst_w, dst_h = surface.get_size() 
    scale, x_off, y_off, render_w, render_h = self.compute_fit(dst_w, dst_h) 
    
    surface.fill(self._background_color) 
    
    if render_w == self._width and render_h == self._height: 
      surface.blit(self.surface, (x_off, y_off)) 
    else: 
      scaled = pygame.transform.smoothscale(self.surface, (render_w, render_h)) 
      surface.blit(scaled, (x_off, y_off)) 
    