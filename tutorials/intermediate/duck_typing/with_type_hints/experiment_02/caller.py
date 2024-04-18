from shapes import Circle, Rectangle, Square
from protocol import Shape

# Use the custom protocol as type-hint.
def describe_shape(shape: Shape):
    print(f"{type(shape).__name__}")
    print(f" Area: {shape.area():.2f}")
    print(f" Perimeter: {shape.perimeter():.2f}")
    print('\n')

describe_shape(Circle(3))

describe_shape(Square(5))

describe_shape(Rectangle(4, 5))