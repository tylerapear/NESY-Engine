import pygame
import sys
from Player import Player

# Set window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Window")
clock = pygame.time.Clock()

player = Player('./assets/Sprites/Player/Down/LinkDown1.png', 50, 50, 100, 100)

# Main loop

running = True
while running:
  dt = clock.tick(60) / 1000

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_s]:
    player.moveDown(dt)
  if keys[pygame.K_w]:
    player.moveUp(dt)
  if keys[pygame.K_a]:
    player.moveLeft(dt)
  if keys[pygame.K_d]:
    player.moveRight(dt)

  # Fill the screen with a color
  screen.fill((30,30,30))

  player.draw(screen)

  pygame.display.flip()

pygame.quit()
sys.exit()
