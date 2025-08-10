import pygame
import os

from classes.entities.Creature import Creature

class Enemy(Creature):
    
  def draw(self, surface):

    self.image = self.animations.getNextImage("Idle")

    """
    self.frameCounter += 1
    if self.frameCounter >= 25:
      self.frameCounter = 0
      self.image = pygame.image.load(self.sprites['Left'][self.animationPhase])
      self.image = pygame.transform.scale(self.image, (self.width, self.height))
      if self.animationPhase >= len(self.sprites['Left']) - 1:
        self.animationPhase = 0
      else:
        self.animationPhase += 1
    """

    surface.blit(self.image, (self.x, self.y))