class Foo():
    def getter(self) -> object:
        return 42
    
    def setter(self, value) -> None:
        raise AttributeError('Cannot change the value')

    attr = property(fget=getter, fset=setter)

my_foo = Foo()
x = my_foo.attr
print(x)
print()

# Error
my_foo.attr = 99