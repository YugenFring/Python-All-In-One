# Implement the descriptor protocol.
class Verbose_attr():
    def __get__(self, obj, type=None) -> object:
        print(obj)
        return 42
    
    def __set__(self, obj, value) -> None:
        raise ValueError('Cannot change the value')

class Foo:
    attr = Verbose_attr()

my_foo = Foo()
# When a descriptor attr is called, the `__get__` method is invoked. 
x = my_foo.attr
print(x)
print()

# Error
my_foo.attr = 99