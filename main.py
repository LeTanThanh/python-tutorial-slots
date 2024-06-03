from point.point_2d import Point2D

# Python __slots__

if __name__ == "__main__":
  ## Introduction to the Python __slots__

  point_2d = Point2D(1, 2)
  # print(point_2d.__dict__)  # AttributeError: 'Point2D' object has no attribute '__dict__'. Did you mean: '__dir__'?
  print(point_2d.__slots__)   # ("x", "y")

  # point_2d.z = 3  # AttributeError: 'Point2D' object has no attribute 'z'

  print(Point2D.__dict__)
  Point2D.color = "black"
  print(Point2D.__dict__)
