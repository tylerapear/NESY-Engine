import pygame
import sys
from classes.entities.Player import Player
from classes.entities.Enemy import Enemy
from classes.effects.Animations import Animations

# Set window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Window")
clock = pygame.time.Clock()

player = Player('./assets/Sprites/Link', 10, 100, 100, 100, 100)
chuchu = Enemy('./assets/Sprites/Enemies/ChuChu', 25, 100, 100, 200, 200)

# Main loop

running = True
while running:
  dt = clock.tick(60) / 1000

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_s]:
    player.moveDown(dt, 200)
  if keys[pygame.K_w]:
    player.moveUp(dt, 200)
  if keys[pygame.K_a]:
    player.moveLeft(dt, 200)
  if keys[pygame.K_d]:
    player.moveRight(dt, 200)

  # Fill the screen with a color
  screen.fill((10,10,10))

  player.draw(screen)
  chuchu.draw(screen)

  pygame.display.flip()

pygame.quit()
sys.exit()
