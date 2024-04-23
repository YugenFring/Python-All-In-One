# Same as experiment_01
class Foo():
    @property
    def attr(self) -> object:
        return 42
    
    @attr.setter
    # Keep this method name same as the property name. 
    def attr(self, value) -> None:
        raise AttributeError('Cannot change the value')

my_foo = Foo()
# Descriptor is invoked under the hood.
x = my_foo.attr
print(x)
print()

# Error
my_foo.attr = 99