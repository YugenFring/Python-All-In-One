from decorators import repeat

@repeat
def say_hi(name):
    print(f"Hi {name}!")

@repeat(num_times=3)
def say_yo(name):
    print(f"Yo {name}!")

say_hi("Fring")
say_yo("Pinkman")