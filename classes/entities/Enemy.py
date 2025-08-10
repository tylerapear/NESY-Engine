import pygame
from classes.entities.Creature import Creature

class Enemy(Creature):
    
  def draw(self, surface):
    self.image = self.animations.getNextImage("Idle")
    surface.blit(self.image, (self.x, self.y))