def say_hi(name):
    print(f'Hi {name}!')

say_hi.__doc__ = 'A simple function that says hi'

print(help(say_hi))