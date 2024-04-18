from typing import Protocol

# Create a `Protocol` subclass to describe the
# required set of methods.
class Shape(Protocol):
    def area(self) -> float: ...

    def perimeter(self) -> float: pass