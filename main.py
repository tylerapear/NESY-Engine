import pygame, sys, asyncio, math 
from classes.entities.Player import Player 
from classes.entities.Enemy import Enemy 
from classes.effects.Animations import Animations 
from classes.entities.items.Sword import Sword 

async def main(): 
  LOGICAL_W, LOGICAL_H = 1280, 720 
  BACKGROUND_COLOR = (24,26,32) 
  
  pygame.init() 
  
  if sys.platform == "win32": 
    try: 
      import ctypes 
      ctypes.windll.shcore.SetProcessDpiAwareness(2) # PMv2 
    except Exception: 
      pass 
    
  flags = pygame.RESIZABLE | pygame.SCALED 
  
  window = pygame.display.set_mode((LOGICAL_W, LOGICAL_H), flags) # Set window size 
  
  RATIO = 16 / 9 
  WIDTH, HEIGHT = 1280, 720 
  icon = pygame.transform.scale(pygame.image.load('./assets/Icons/GameIcon.png'), (132,132)) 
  pygame.display.set_icon(icon) 
  screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) 
  pygame.display.set_caption("The Legend of Xelda") 
  clock = pygame.time.Clock() 
  hitboxes_visible = False 
  logical_surface = pygame.Surface((LOGICAL_W, LOGICAL_H), pygame.SRCALPHA, 32) 
  
  def font(px): return pygame.font.SysFont(None, px, bold=False) 
  
  def compute_fit(dst_w, dst_h, src_w=LOGICAL_W, src_h=LOGICAL_H): 
    scale = min(dst_w / src_w, dst_h / src_h) 
    render_w, render_h = int(src_w * scale), int(src_h * scale) 
    x_off = (dst_w - render_w) // 2 
    y_off = (dst_h - render_h) // 2 
    return scale, x_off, y_off, render_w, render_h 
  
  def window_to_logical(win_pos, dst_size): 
    x, y = win_pos 
    dst_w, dst_h = dst_size 
    scale, x_off, y_off, render_w, render_h = compute_fit(dst_w, dst_h) 
    
  def blit_logical_to_window(): 
    win_surf = pygame.display.get_surface() 
    dst_w, dst_h = win_surf.get_size() 
    scale, x_off, y_off, render_w, render_h = compute_fit(dst_w, dst_h) 
    
    win_surf.fill(BACKGROUND_COLOR) 
    
    if render_w == LOGICAL_W and render_h == LOGICAL_H: 
      win_surf.blit(logical_surface, (x_off, y_off)) 
    else: 
      scaled = pygame.transform.smoothscale(logical_surface, (render_w, render_h)) 
      win_surf.blit(scaled, (x_off, y_off)) 
      
  game_over_font = font(36)     
  
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
    
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        running = False 
      elif event.type == pygame.VIDEORESIZE: 
        pass 
      elif event.type == pygame.MOUSEBUTTONDOWN: 
        pos_logical = window_to_logical(event.pos, pygame.display.get_surface().get_size()) 
        if pos_logical: 
          print("Logical click at: ", (round(pos_logical[0], 1), round(pos_logical[1], 1))) 
        else: 
          print("Clicked in") 
          
    player.update(dt, logical_surface, chuchus, player.inventory[0]) 
    for chuchu in chuchus: 
      chuchu.update(dt, player.inventory[0]) 
      
    # Fill the screen with a color  
    logical_surface.fill((10,10,10)) 
    
    if player.checkForGameOver(): 
      gameover_surface = game_over_font.render("GAME OVER", True, (255,255,255)) 
      logical_surface.blit(gameover_surface, (300,20)) 
    
    player.draw(logical_surface) 
    player.inventory[0].drawHitbox(logical_surface) 
    
    for chuchu in chuchus: 
      chuchu.draw(logical_surface) 
    
    blit_logical_to_window()
    pygame.display.flip() 
    await asyncio.sleep(0) 
    
asyncio.run(main()) 