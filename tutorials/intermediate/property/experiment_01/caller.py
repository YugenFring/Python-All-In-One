class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    
    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y
    
    def set_y(self, value):
        return self._y
    

point = Point(12, 5)

print(point.get_x())
print(point.get_y())
print()

point.set_x(99)
print(point.get_x())
print()

print(point._x)
print(point._y)