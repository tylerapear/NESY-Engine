import pygame
from classes.entities.Tile import Tile
from classes.entities.Hitbox import Hitbox

class DummyScreen:
    def __init__(self, tile_width, tile_height):
        self.tile_width = tile_width
        self.tile_height = tile_height

def test_draw_background():
    screen = DummyScreen(100, 50)
    tile = Tile("assets/Tiles/sand.png")
    surface = pygame.Surface((400, 300))

    # Call draw_background and ensure no exceptions are raised
    tile.draw_background(screen, surface, 10, 20)

def test_draw_foreground_and_hitbox():
    screen = DummyScreen(100, 50)
    tile = Tile(
        "assets/Tiles/sand.png",
        "assets/Tiles/mountain.png",
        hitbox_active=True,
        hitbox_offset={"x": 0.1, "y": 0.2, "width": 0.5, "height": 0.6},
    )
    surface = pygame.Surface((400, 300))

    # Call draw_foreground and ensure hitbox is updated correctly
    tile.draw_foreground(screen, surface, 10, 20)

    assert tile.hitbox.x == 10 + screen.tile_width * 0.1
    assert tile.hitbox.y == 20 + screen.tile_height * 0.2
    assert tile.hitbox.width == screen.tile_width * 0.5
    assert tile.hitbox.height == screen.tile_height * 0.6