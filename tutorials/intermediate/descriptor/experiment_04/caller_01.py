# Descriptors are instantiated just once per class.
# Every single instance of a class containing a descriptor
# shares that this descriptor instance.
class OneDigitNumbericValue():
    def __init__(self):
        self.value = 0

    def __get__(self, obj, type=None) -> object:
        # `self`` is the instance of the descriptor you're writing.
        # `obj` is the instance of the object your descriptor is attached to.
        # `type` is the type of the object the descriptor is attached to.
        return self.value
    
    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError('The vaue is invalid')
        self.value = value

class Foo():
    number = OneDigitNumbericValue()

my_first_foo = Foo()
my_second_foo = Foo()

my_first_foo.number = 3
print(my_first_foo.number)
print(my_second_foo.number)

my_third_foo = Foo()
print(my_third_foo.number)