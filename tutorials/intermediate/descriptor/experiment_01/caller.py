# Implement the descriptor protocol.
class Verboase_attr():
    def __get__(self, obj, type=None) -> object:
        return 42
    
    def __set__(self, obj, value) -> None:
        raise ValueError('Cannot change the value')


class Foo:
    attr = Verboase_attr()


my_foo = Foo()
x = my_foo.attr
print(x)
print()

my_foo.attr = 99