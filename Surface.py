import Rectangle
class Surface:
  def __init__(self, filename, x, y, w, h):
    self.rect = Rectangle.Rectangle(x, y, w, h)
    self.image = filename

  def getRect(self):
    return self.rect
    