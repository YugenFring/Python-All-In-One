from decorators import repeat

# Decorators with arguments
@repeat(num_times=4)
def say_hi(name):
    print(f"Hello {name}!")

say_hi("Fring")