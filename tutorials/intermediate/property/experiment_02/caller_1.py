class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def _get_x(self):
        return self._x
    
    def _get_y(self):
        return self._y
    
    def _set_x(self, value):
        self._x = value

    def _set_y(self, value):
        self._y = value

    def _del_x(self):
        del self._x

    def _del_y(self):
        del self_y

    x = property(
        fget=_get_x,
        fset=_set_x,
        fdel=_del_x,
        doc='The x point.'
    )

    y = property(
        fget=_get_y,
        fset=_set_y,
        fdel=_del_y,
        doc='The y point.'
    )
    

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