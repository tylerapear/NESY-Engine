import pygame
import sys
from Player import Player

# Set window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Window")

player = Player('./assets/Link.png', 50, 50, 100, 100)

# Main loop

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Fill the screen with a color
  screen.fill((30,30,30))

  player.draw(screen)

  pygame.display.flip()

pygame.quit()
sys.exit()
