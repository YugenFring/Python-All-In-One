from decorators import do_twice

@do_twice
def say_hi(name):
    print(f"Hi, {name}!")

say_hi("Fring")