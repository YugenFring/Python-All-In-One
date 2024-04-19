class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value

    @y.deleter
    def x(self):
        del self._y


point = Point(12, 5)

print(point.x)
print(point.y)
print()

point.x = 24
point.y = 50
print(point.x)
print(point.y)
print()

del point.x
print(point.__dict__)
print()

print(help(point))
print()

# Show all the attrs and methods.
print(dir(Point.x))