class OneDigitNumbericValue():
    def __set_name__(self, owner, name):
        # Owner is the class type of the object your descriptor
        # is attached to.
        # Whenever you instantiate a descriptor this method
        # is called and the `name` automatically set.
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0
    
    def __set__(self, obj, value) -> object:
        obj.__dict__[self.name] = value

class Foo():
    number = OneDigitNumbericValue()

my_first_foo = Foo()
my_second_foo = Foo()

my_first_foo.number = 3
print(my_first_foo.number)
print(my_second_foo.number)

my_third_foo = Foo()
print(my_third_foo.number)