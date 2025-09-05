import pygame, sys, asyncio, math 
from classes.entities.Player import Player 
from classes.entities.Enemy import Enemy 
from classes.effects.Animations import Animations 
from classes.entities.items.Sword import Sword
from classes.entities.LogicalSurface import LogicalSurface

async def main(): 
  
  pygame.init() 
    
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
  
  player = Player( 
    spritePath = './assets/Sprites/Link', 
    animationSpeed = 10, 
    width = 250, 
    height = 250, 
    x = 200, 
    y = 100, 
    hitbox_dimentions = {"x": 288, "y": 188, "width": 75, "height": 75}, 
    hitbox_visible = hitboxes_visible 
  ) 
  chuchus = [ 
    Enemy( 
      spritePath = './assets/Sprites/Enemies/ChuChu', 
      animationSpeed = 25, 
      width = 100, 
      height = 100, 
      x = 400, 
      y = 400, 
      hitbox_dimentions = {"x": 410, "y": 415, "width": 85, "height": 80}, 
      hitbox_visible = hitboxes_visible 
    ) 
  ] 
  
  player.inventory.append( 
    Sword( 
      player = player, 
      hitbox_visible = hitboxes_visible 
    ) 
  ) 
  
  # Main Loop 
  
  running = True 
  while running: 
    dt = clock.tick(60) / 1000 
    
    # CHECK FOR WINDOW EVENTS #
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        running = False 
          
    if player.alive:
      # UPDATE ENTITIES #
      player.update(dt, logical_surface.surface, chuchus, player.inventory[0]) 
      for chuchu in chuchus: 
        chuchu.update(dt, player.inventory[0]) 
        
      # FILL THE SCREEN BACKGROUND COLOR #
      logical_surface.surface.fill((10,10,10)) 
      
      # CHECK FOR GAME OVER #
      if player.checkForGameOver(): 
        gameover_surface = game_over_font.render("GAME OVER", True, (255,255,255)) 
        logical_surface.surface.blit(gameover_surface, (300,20)) 
      
      # DRAW ENTITIES #
      player.draw(logical_surface.surface) 
      player.inventory[0].drawHitbox(logical_surface.surface) 
      for chuchu in chuchus: 
        chuchu.draw(logical_surface.surface) 
    
    # DRAW RESIZED LOGICAL SCREEN ON WINDOW #
    #blit_logical_to_window()
    logical_surface.blit(pygame.display.get_surface())
    
    # UPDATE WINDOW #
    pygame.display.flip() 
    await asyncio.sleep(0) 
    
asyncio.run(main()) 