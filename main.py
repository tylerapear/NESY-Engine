import pygame
import sys

print("hello world")

# Set window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Window")

# Main loop

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Fill the screen with a color
  screen.fill((30,30,30))
  pygame.display.flip()

pygame.quit()
sys.exit()
