import pygame
from classes.entities.PlayerCopy import Player
from classes.entities.items.Sword import Sword
from classes.effects.Animation import Animation
from classes.entities.LogicalSurface import LogicalSurface
from data.worldMap2x2 import buildMap

pygame.init()

LOGICAL_W, LOGICAL_H = 1280, 720 
BACKGROUND_COLOR = (24,26,32) 
pygame.display.set_mode((LOGICAL_W, LOGICAL_H), pygame.RESIZABLE) 

clock = pygame.time.Clock()

logical_surface = LogicalSurface(LOGICAL_W, LOGICAL_H, BACKGROUND_COLOR)

player_animations = {
    "Up": Animation("./assets/Sprites/Link/Up", 10, 250, 250),
    "Down": Animation("./assets/Sprites/Link/Down", 10, 250, 250),
    "Left": Animation("./assets/Sprites/Link/Left", 10, 250, 250),
    "Right": Animation("./assets/Sprites/Link/Right", 10, 250, 250)
}

player = Player( 
    spritePath = './assets/Sprites/Link', 
    animationSpeed = 10,
    animations = player_animations,
    width = 250, 
    height = 250, 
    health = 60,
    x = 200, 
    y = 100, 
    hitbox_offset_dimentions = {"x": 88, "y": 88, "width": 75, "height": 75}, 
    hitbox_visible = False
)

active_enemies = []

world_map = buildMap()

running = True
while running: 
    dt = clock.tick(60) / 1000 
    
    # CHECK FOR WINDOW EVENTS #
    events = pygame.event.get()
    for event in events: 
      if event.type == pygame.QUIT: 
        running = False
      
    player.inventory.append( 
    Sword( 
        player = player, 
        hitbox_visible = False 
    ) 
    ) 
          
    player.update(dt, world_map, logical_surface.surface, active_enemies, player.inventory[0])
      
    # FILL THE SCREEN BACKGROUND COLOR #
    logical_surface.surface.fill((10,10,10)) 
    
    # DRAW ENTITIES #
    player.draw(logical_surface.surface) 
    player.inventory[0].drawHitbox(logical_surface.surface)
    
    # DRAW RESIZED LOGICAL SCREEN ON WINDOW #
    pygame.display.get_surface().blit(logical_surface.surface, (0,0))
    
    # UPDATE WINDOW #
    pygame.display.flip() 