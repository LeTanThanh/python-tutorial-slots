from .point_2d import Point2D

class Point3D(Point2D):
  __slots__ = ("z",)
  def __init__(self, x, y, z) -> None:
    super().__init__(x, y)
    self.z = z
