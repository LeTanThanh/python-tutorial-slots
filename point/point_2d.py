from .shape import Shape
class Point2D(Shape):
  __slots__ = ("x", "y")

  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y

  def __repr__(self):
    return f"Point2D({self.x}, {self.y})"
