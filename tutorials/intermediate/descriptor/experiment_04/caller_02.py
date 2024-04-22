# Try to avoid sharing the same value between all instances.
class OneDigitNumbericValue():
    def __init__(self):
        self.value = {}

    def __get__(self, obj, type=None) -> object:
        try:
            return self.value[obj]
        except:
            return 0
    
    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError('The vaue is invalid')
        self.value[obj] = value

class Foo():
    number = OneDigitNumbericValue()

my_first_foo = Foo()
my_second_foo = Foo()

my_first_foo.number = 3
print(my_first_foo.number)
print(my_second_foo.number)

my_third_foo = Foo()
print(my_third_foo.number)

# Unfortunately, the downside here is that the descriptor is keeping a stroing reference to the
# owner object. This means that if you destroy the object, then the memeory is not released
# bacause the garbage collector keeps finding a reference to that object inside the descriptor!