

class WorldMap():
  def __init__(self, screens_wide, screens_high, screens, start_screen_index):
    self._screens_wide = screens_wide
    self._screens_high = screens_high
    self._screens = screens
    self._start_screen_index = start_screen_index
    self._current_screen = screens[start_screen_index]
    
### PROPERTIES ###

  @property
  def screens_wide(self):
    return self._screens_wide
  
  @screens_wide.setter
  def screens_wide(self, screens_wide):
    self._screens_wide = screens_wide
    
  @property
  def screens_high(self):
    return self._screens_high
  
  @screens_high.setter
  def screens_high(self, screens_high):
    self._screens_high = screens_high
    
  @property
  def screens(self):
    return self._screens
  
  @screens.setter
  def screens(self, screens):
    self._screens = screens
    
  @property
  def start_screen_index(self):
    return self._start_screen_index
  
  @start_screen_index.setter
  def start_screen_index(self, start_screen_index):
    self._start_screen_index = start_screen_index
    
  @property
  def current_screen(self):
    return self._current_screen
  
  @current_screen.setter
  def current_screen(self, current_screen):
    self._current_screen = current_screen
    
### METHODS ###

  def setNextScreen(self, direction):
    next_screen = self.getNextScreen(direction)
    if next_screen:
      self.current_screen = self.getNextScreen(direction)
    return next_screen
  
  def getScreenIfExists(self, screen_index):
    if screen_index < len(self.screens):
      return self.screens[screen_index]
    return None
  
  def getNextScreen(self, direction):
    if direction == "Up":
      if self.screens.index(self.current_screen) + 1 <= self.screens_wide:
        return None
      return self.getScreenIfExists(self.screens.index(self.current_screen) - self.screens_wide)
    elif direction == "Down":
      if self.screens.index(self.current_screen) + 1 > len(self.screens) - self.screens_wide:
        return None
      return self.getScreenIfExists(self.screens.index(self.current_screen) + self.screens_wide)
    elif direction == "Left":
      if (self.screens.index(self.current_screen) + 1) % self.screens_wide == 1:
        return None
      return self.getScreenIfExists(self.screens.index(self.current_screen) - 1)
    elif direction == "Right":
      if (self.screens.index(self.current_screen) + 1) % self.screens_wide == 0:
        return None
      return self.getScreenIfExists(self.screens.index(self.current_screen) + 1)