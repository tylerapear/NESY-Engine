import pygame
from classes.entities.Creature import Creature

class Enemy(Creature):

  def update(self, dt):
    self.image = self.animations.getNextImage("Idle")
    
  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))

    #TODO: REMOVE LINE
    self.hitbox.draw(surface) 