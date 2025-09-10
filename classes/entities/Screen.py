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
    
  def draw(self, surface):
    draw_position = [0,0]
    tile_index = 0
    for vertical_tile in range(self._tiles_high):
      for horizontal_tile in range(self._tiles_wide):
        tile = self._tiles[tile_index]
        scaled_image = pygame.transform.scale(
          tile._background_image, (self._tile_width, self._tile_height)
        )
        surface.blit(scaled_image, (draw_position[0], draw_position[1]))
        draw_position[0] += self._tile_width
      draw_position[0] = 0
      draw_position[1] += self._tile_height
        