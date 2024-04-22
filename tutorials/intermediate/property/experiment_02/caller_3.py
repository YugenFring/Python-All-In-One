class WriteCoordinateError(Exception):
    pass


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        raise WriteCoordinateError("x coordinate is read-only")

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        raise WriteCoordinateError("x coordinate is read-only")

point = Point(12, 5)

point.x = 24
point.y = 50
print(point.x)
print(point.y)
print()