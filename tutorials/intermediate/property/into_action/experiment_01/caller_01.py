# Validating input values
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
        except ValueError:
            raise ValueError('`x` must be a number') from None
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
        except ValueError:
            raise ValueError('`y` must be a number') from None
        

point = Point(12, 5)
print(point.x, point.y)
print()

point.x = 'one'