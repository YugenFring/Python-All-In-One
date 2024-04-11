from decorators import do_twice

@do_twice
def say_hi(name):
    print("Hi, {name}!")
    return True

# Get return value from decorator.
r = say_hi("Fring")
print(r)