class Rectangle:
  def __init__(self, x, y, h, w):
    self.x = x
    self.y = y
    self.width = w
    self.height = h
    
    if self.x < 0:
      self.x = 0
    elif self.y < 0:
      self.y = 0
    elif self.width < 0:
      self.width = 0
    elif self.height < 0:
      self.height = 0

    
  def  __str__(self):
    self.string = f"{self.x}, {self.y}, {self.width}, {self.height}"
    
    return self.string
  