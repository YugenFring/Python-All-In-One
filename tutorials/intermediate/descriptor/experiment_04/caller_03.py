# Store values in the object that the descriptor is attached to.
class OneDigitNumbericValue():
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0
    
    def __set__(self, obj, value) -> object:
        obj.__dict__[self.name] = value

class Foo():
    number = OneDigitNumbericValue('number')

my_first_foo = Foo()
my_second_foo = Foo()

my_first_foo.number = 3
print(my_first_foo.number)
print(my_second_foo.number)

my_third_foo = Foo()
print(my_third_foo.number)