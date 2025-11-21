import pygame
from classes.entities.Player import Player
from classes.entities.items.Sword import Sword
from classes.effects.Animation import Animation
from classes.entities.LogicalSurface import LogicalSurface
from classes.entities.WanderingEnemy import WanderingEnemy
from data.worldMap2x2 import buildMap

pygame.init()

LOGICAL_W, LOGICAL_H = 1280, 720 
BACKGROUND_COLOR = (24,26,32)
FRAMERATE = 60
MILLISECONDS_PER_SECOND = 1000
pygame.display.set_mode((LOGICAL_W, LOGICAL_H), pygame.RESIZABLE) 

clock = pygame.time.Clock()

logical_surface = LogicalSurface(LOGICAL_W, LOGICAL_H, BACKGROUND_COLOR)

player_animations = {
    "IdleUp": Animation("./assets/Sprites/Link/IdleUp", 10, 250, 250),
    "IdleDown": Animation("./assets/Sprites/Link/IdleDown", 10, 250, 250),
    "IdleLeft": Animation("./assets/Sprites/Link/IdleLeft", 10, 250, 250),
    "IdleRight": Animation("./assets/Sprites/Link/IdleRight", 10, 250, 250),
    "Up": Animation("./assets/Sprites/Link/Up", 50, 250, 250),
    "Down": Animation("./assets/Sprites/Link/Down", 50, 250, 250),
    "Left": Animation("./assets/Sprites/Link/Left", 50, 250, 250),
    "Right": Animation("./assets/Sprites/Link/Right", 50, 250, 250),
    "AttackUp": Animation("./assets/Sprites/Link/AttackUp", 10, 250, 250),
    "AttackDown": Animation("./assets/Sprites/Link/AttackDown", 10, 250, 250),
    "AttackLeft": Animation("./assets/Sprites/Link/AttackLeft", 10, 250, 250),
    "AttackRight": Animation("./assets/Sprites/Link/AttackRight", 10, 250, 250),
    "Death": Animation("./assets/Sprites/Link/Death", 50, 250, 250)
    
}

enemy_animations = {
    "Idle": Animation("./assets/Sprites/Enemies/ChuChu/Idle", 10, 250, 250),
    
}

player = Player(  
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

enemy = WanderingEnemy( 
          animationSpeed = 25,
          animations = enemy_animations,
          width = 100, 
          height = 100,
          health = 30,
          x = 1000, 
          y = 150, 
          hitbox_offset_dimentions = {"x": 10, "y": 15, "width": 85, "height": 80}, 
          hitbox_visible = False
)

active_enemies = [enemy]

world_map = buildMap()

running = True
while running and player.alive: 
    dt = clock.tick(FRAMERATE) / MILLISECONDS_PER_SECOND 
    
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
          
    player.update(dt, FRAMERATE, world_map, logical_surface.surface, active_enemies, player.inventory[0])
    enemy.update(dt, FRAMERATE, world_map, player.inventory[0])
      
    # FILL THE SCREEN BACKGROUND COLOR #
    logical_surface.surface.fill((10,10,10)) 
    
    # DRAW ENTITIES #
    player.draw(logical_surface.surface) 
    player.inventory[0].drawHitbox(logical_surface.surface)
    enemy.draw(logical_surface.surface)
    
    # DRAW RESIZED LOGICAL SCREEN ON WINDOW #
    pygame.display.get_surface().blit(logical_surface.surface, (0,0))
    
    # UPDATE WINDOW #
    pygame.display.flip() 