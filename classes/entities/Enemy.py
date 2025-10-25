from classes.entities.Creature import Creature

class Enemy(Creature):

### PROPERTIES ###

### METHODS ###

  def update(self, dt, world_map, weapon):
    super().update(dt, world_map)
    if not self.alive:
      return #their update logic wont run if the enemies die
    if weapon.active and self.immunity_count <= 0:
      self.checkForDamage(weapon)
    
  def draw(self, surface):
    super().draw(surface)
    surface.blit(self.image, (self.x, self.y))

  def checkForDamage(self, weapon):
    if self.hitbox.collides(weapon.hitbox):
      self.damage_direction = weapon.direction
      self.takeDamage(weapon.damage)