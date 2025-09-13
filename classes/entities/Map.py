

class Map():
  def __init__(self, screens_wide, screens_high, screens):
    self._screens_wide = screens_wide
    self._screens_high = screens_high
    self._screens = screens
    
### PROPERTIES ###

  @property
  def screens_wide(self):
    return self._screens_wide
  
  @screens_wide.setter
  def screens_wide(screens_wide):
    self._screens_wide = screens_wide
    
    @property
  def screens_high(self):
    return self._screens_high
  
  @screens_high.setter
  def screens_high(screens_high):
    self._screens_high = screens_high
    
    @property
  def screens(self):
    return self._screens
  
  @screens.setter
  def screens(screens):
    self._screens = screens