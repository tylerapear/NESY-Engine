import pygame
import sys
from classes.entities.Player import Player
from classes.entities.Enemy import Enemy
from classes.effects.Animations import Animations

pygame.init()

# Set window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("The Legend of Xelda")
icon = pygame.transform.scale(pygame.image.load('./assets/Icons/GameIcon.png'), (132,132))
pygame.display.set_icon(icon)
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

player = Player(
  spritePath = './assets/Sprites/Link', 
  animationSpeed = 10, 
  width = 250, 
  height = 250, 
  x = 200, 
  y = 100, 
  hitbox_width = 75, 
  hitbox_height = 75, 
  hitbox_x = 288, 
  hitbox_y = 188,
  hitbox_visible = True
)
chuchu = Enemy('./assets/Sprites/Enemies/ChuChu', 25, 100, 100, 400, 400, 85, 80, 410, 415, True)

# Main loop

running = True
while running:
  dt = clock.tick(60) / 1000

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  player.update(dt, [chuchu])
  chuchu.update(dt)

  # Fill the screen with a color
  screen.fill((10,10,10))
  text_surface = font.render(str(player.health), True, (255,255,255))
  screen.blit(text_surface, (20,20))

  if player.checkForGameOver():
    gameover_surface = font.render("GAME OVER", True, (255,255,255))
    screen.blit(gameover_surface, (300,20))

  player.draw(screen)
  chuchu.draw(screen)

  pygame.display.flip()

pygame.quit()
sys.exit()
