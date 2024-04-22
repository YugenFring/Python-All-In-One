class Point:
    """Assume that the value of y is twice that of x. """
    def __init__(self, x):
        # Unlike before, it makes x a `float`.
        self.x = x
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = float(value)

    @property
    def y(self):
        return self.x * 2
    
    @y.setter
    def y(self, value):
        self.x = value / 2


point = Point(x=2)
print(point.x)
print(point.y)
print()

point.y = 40
print(point.x)