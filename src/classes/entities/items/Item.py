

class Item:
  def __init__(self):
    self._equipped = False
    self._active = False

### PROPERTIES ###

  @property
  def equipped(self):
    return self._equipped

  @equipped.setter
  def equipped(self, equipped):
    self._equipped = equipped

  @property
  def active(self):
    return self._active

  @active.setter
  def active(self, active):
    self._active = active

### METHODS ###

  def update(self, player):
    self.direction = player.direction