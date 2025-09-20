import pygame, sys, asyncio, math, copy

pygame.init() 

from classes.effects.TextSurface import TextSurface
from classes.entities.Player import Player 
from classes.entities.items.Sword import Sword
from classes.entities.LogicalSurface import LogicalSurface
from classes.entities.WorldMap import WorldMap


from data.worldMap2x2 import buildMap
# from data.TestMap3x3 import screens

async def main(): 
    
  # SET WINDOW PROPERTIES #
  LOGICAL_W, LOGICAL_H = 1280, 720 
  BACKGROUND_COLOR = (24,26,32) 
  window = pygame.display.set_mode((LOGICAL_W, LOGICAL_H), pygame.RESIZABLE) 
  icon = pygame.transform.scale(pygame.image.load('./assets/Icons/GameIcon.png'), (132,132)) 
  pygame.display.set_icon(icon)  
  pygame.display.set_caption("The Legend of Xelda") 
  
  # SET OTHER PROPERTIES #
  clock = pygame.time.Clock() 
  hitboxes_visible = False    
  game_over_font = pygame.font.SysFont(None, 36, bold=False)

  # DEFINE ENTITIES # 
  logical_surface = LogicalSurface(LOGICAL_W, LOGICAL_H, BACKGROUND_COLOR)     
  
  def drawGameoverScreen():
    TextSurface(
        background_color = (0,0,0),
        width = LOGICAL_W,
        height = LOGICAL_H
    ).draw(logical_surface.surface)

    TextSurface(
      text_content = "GAME OVER",
      background_color = (15,15,15),
      opacity = 0,
      border_thickness = 0,
      text_color = (255,0,0),
      x_position = 20,
      y_position = 120,
      width = LOGICAL_W - 40,
      height = LOGICAL_H / 4,
      horizontal_alignment = "center",
      font_size = 128
    ).draw(logical_surface.surface)
    
    TextSurface(
      text_content = "Press 'Y' to play again",
      background_color = (15,15,15),
      opacity = 0,
      border_thickness = 0,
      text_color = (255,255,255),
      x_position = 20,
      y_position = 350,
      width = LOGICAL_W - 40,
      height = LOGICAL_H / 4,
      horizontal_alignment = "center",
      font_size = 48
    ).draw(logical_surface.surface)
  
  # Main Loop 
  
  running = True 
  first_frame = True
  while running: 
    dt = clock.tick(60) / 1000 
    
    # CHECK FOR WINDOW EVENTS #
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        running = False
        
    # IF FIRST FRAME, SET UP MAP AND PLAYER
    if first_frame:
      first_frame = False
      
      world_map = buildMap() #used for worldMap2x2
      #world_map = WorldMap(3,3, screens, 0) #used for TestMap3x3
      
      player = Player( 
        spritePath = './assets/Sprites/Link', 
        animationSpeed = 10, 
        width = 250, 
        height = 250, 
        health = 60,
        x = 200, 
        y = 100, 
        hitbox_offset_dimentions = {"x": 88, "y": 88, "width": 75, "height": 75}, 
        hitbox_visible = hitboxes_visible
      ) 
  
      player.inventory.append( 
        Sword( 
          player = player, 
          hitbox_visible = hitboxes_visible 
        ) 
      ) 
        
    active_enemies = [creature for creature in world_map.current_screen.creatures if creature.alive]
          
    if player.alive:
      # UPDATE ENTITIES #
      player.update(dt, world_map, logical_surface.surface, active_enemies, player.inventory[0])
      
      world_map.current_screen.update(dt, world_map, player.inventory[0])
      
      # FILL THE SCREEN BACKGROUND COLOR #
      logical_surface.surface.fill((10,10,10)) 
      
      # CHECK FOR GAME OVER #
      if player.checkForGameOver(): 
        gameover_surface = game_over_font.render("GAME OVER", True, (255,255,255)) 
        logical_surface.surface.blit(gameover_surface, (300,20)) 
      
      # DRAW ENTITIES #
      world_map.current_screen.draw(logical_surface.surface)
      player.draw(logical_surface.surface) 
      player.inventory[0].drawHitbox(logical_surface.surface)
      
      #drawTextSurface(logical_surface.surface, textSurface)
      
    else:
      #GAME OVER
      drawGameoverScreen()
      keys = pygame.key.get_pressed()
      if keys[pygame.K_y]:
        first_frame = True
    
    # DRAW RESIZED LOGICAL SCREEN ON WINDOW #
    logical_surface.blit(pygame.display.get_surface())
    
    # UPDATE WINDOW #
    pygame.display.flip() 
    await asyncio.sleep(0) 
    
asyncio.run(main()) 
