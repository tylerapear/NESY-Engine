import pygame
from classes.entities.Creature import Creature

class Enemy(Creature):

  def checkForDamage(self, weapon):
    if self.hitbox.collides(weapon.hitbox):
      self.damage_direction = weapon.direction
      self.takeDamage(weapon.damage)

  def update(self, dt, weapon):
    super().update(dt)
    if weapon.active and self.immunity_count <= 0:
      self.checkForDamage(weapon)
    
  def draw(self, surface):
    super().draw(surface)
    surface.blit(self.image, (self.x, self.y))