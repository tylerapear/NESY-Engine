from src.classes.entities.Creature import Creature

class Enemy(Creature):

### PROPERTIES ###

### METHODS ###

  def update(self, dt, FRAMERATE, world_map, weapon):
    super().update(dt, FRAMERATE, world_map)
    if not self.alive:
      return #their update logic wont run if the enemies die
    if weapon.active and self.immunity_count <= 0:
      self.checkForDamage(weapon)
    
  def draw(self, surface):
    super().draw(surface)

  def checkForDamage(self, weapon):
    if self.immunity_count > 0:
      return
    if self.hitbox.collides(weapon.hitbox):
      self.damage_direction = weapon.direction
      self.takeDamage(weapon.damage)