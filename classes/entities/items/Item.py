

class Item:
  def __init__(self):
    self.equipped = False
    self.active = False

  def update(self, player):
    self.direction = player.direction