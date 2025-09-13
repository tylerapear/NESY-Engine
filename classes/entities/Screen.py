from classes.entities.Tile import Tile
import pygame

class Screen():
  
  def __init__(self, width, height, tiles_wide, tiles_high, tiles):
    self._width = width
    self._height = height
    self._tiles_wide = tiles_wide
    self._tiles_high = tiles_high
    self._tile_width = width // tiles_wide
    self._tile_height = height // tiles_high
    self._tiles = tiles
    self._active = False
    
### PROPERTIES ###
  
  @property
  def width(self):
    return self._width
  
  @width.setter
  def width(width):
    self._width = width
    
  @property
  def height(self):
    return self._height
  
  @height.setter
  def height(height):
    self._height = height
    
  @property
  def tiles_wide(self):
    return self._tiles_wide
  
  @tiles_wide.setter
  def tiles_wide(tiles_wide):
    self._tiles_wide = tiles_wide
    
  @property
  def tiles_high(self):
    return self._tiles_high
  
  @tiles_high.setter
  def tiles_high(tiles_high):
    self._tiles_high = tiles_high
    
  @property
  def tile_width(self):
    return self._tile_width
  
  @tile_width.setter
  def tile_width(tile_width):
    self._tile_width = tile_width
    
  @property
  def tile_height(self):
    return self._tile_height
  
  @tile_height.setter
  def tile_height(tile_height):
    self._tile_height = tile_height
    
  @property
  def tiles(self):
    return self._tiles
  
  @tiles.setter
  def tiles(tiles):
    self._tiles = tiles
    
  @property
  def active(self):
    return self._active
  
  @active.setter
  def active(active):
    self._active = active
  
### METHODS ###
    
  def draw(self, surface):
    draw_position = [0,0]
    tile_index = 0
    for vertical_tile in range(self.tiles_high):
      for horizontal_tile in range(self.tiles_wide):
        tile = self.tiles[tile_index]
        tile.draw_background(self, surface, draw_position[0], draw_position[1])
        draw_position[0] += self.tile_width
        if tile_index < len(self.tiles) - 1:
          tile_index += 1
      draw_position[0] = 0
      draw_position[1] += self.tile_height
      
    draw_position = [0,0]
    tile_index = 0
    for vertical_tile in range(self.tiles_high):
      for horizontal_tile in range(self.tiles_wide):
        tile = self.tiles[tile_index]
        tile.draw_foreground(self, surface, draw_position[0], draw_position[1])
        draw_position[0] += self.tile_width
        if tile_index < len(self.tiles) - 1:
          tile_index += 1
      draw_position[0] = 0
      draw_position[1] += self.tile_height
        