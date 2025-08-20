import pygame
import sys
from classes.entities.Player import Player
from classes.entities.Enemy import Enemy
from classes.effects.Animations import Animations
from classes.entities.items.Sword import Sword

pygame.init()

# Set window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("The Legend of Xelda")
icon = pygame.transform.scale(pygame.image.load('./assets/Icons/GameIcon.png'), (132,132))
pygame.display.set_icon(icon)
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
hitboxes_visible = False

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

# Main loop

running = True
while running:
  dt = clock.tick(60) / 1000

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  player.update(dt, screen, chuchus, player.inventory[0])
  for chuchu in chuchus:
    chuchu.update(dt, player.inventory[0])

  # Fill the screen with a color
  screen.fill((10,10,10))

  if player.checkForGameOver():
    gameover_surface = font.render("GAME OVER", True, (255,255,255))
    screen.blit(gameover_surface, (300,20))

  player.draw(screen)
  player.inventory[0].drawHitbox(screen)
  for chuchu in chuchus:
    chuchu.draw(screen)

  pygame.display.flip()
  #print("frame")

pygame.quit()
sys.exit()
