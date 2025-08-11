import pygame
import sys
from classes.entities.Player import Player
from classes.entities.Enemy import Enemy
from classes.effects.Animations import Animations

# Set window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("The Legend of Xelda")
icon = pygame.transform.scale(pygame.image.load('./assets/Icons/GameIcon.png'), (132,132))
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

player = Player(
  spritePath = './assets/Sprites/Link', 
  animationSpeed = 10, 
  width = 250, 
  height = 250, 
  x = 200, 
  y = 200, 
  hitbox_width = 75, 
  hitbox_height = 75, 
  hitbox_x = 288, 
  hitbox_y = 288,
  hitbox_visible = True
)
chuchu = Enemy('./assets/Sprites/Enemies/ChuChu', 25, 100, 100, 50, 50, 85, 80, 60, 65, True)

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

  player.draw(screen)
  chuchu.draw(screen)

  pygame.display.flip()

pygame.quit()
sys.exit()
