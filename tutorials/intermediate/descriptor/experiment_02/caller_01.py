# Same as experiment_01
class Foo():
    @property
    def attr(self) -> object:
        return 42
    
    @attr.setter
    def attr(self, value) -> None:
        raise AttributeError('Cannot change the value')


my_foo = Foo()
x = my_foo.attr
print(x)
print()

my_foo.attr = 99