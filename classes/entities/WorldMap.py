

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
    self.current_screen = self.getNextScreenIndex(direction)
  
  def getNextScreenIndex(self, direction):
    if direction == "Up":
      return self.screens[self.screens.index(self.current_screen) - self.screens_wide]
    elif direction == "Down":
      return self.screens[self.screens.index(self.current_screen) + self.screens_wide]
    elif direction == "Left":
      return self.screens[self.screens.index(self.current_screen) - 1]
    elif direction == "Right":
      return self.screens[self.screens.index(self.current_screen) + 1]