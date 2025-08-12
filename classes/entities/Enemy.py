import pygame
from classes.entities.Creature import Creature

class Enemy(Creature):

  def checkForDamage(self, weapon):
    if self.hitbox.collides(weapon.hitbox):
      self.takeDamage(weapon.damage)

  def update(self, dt, weapon):
    super().update()
    self.image = self.animations.getNextImage("Idle")
    if weapon.active and self.immunity_count <= 0:
      self.checkForDamage(weapon)
    
  def draw(self, surface):
    super().draw(surface)
    surface.blit(self.image, (self.x, self.y))