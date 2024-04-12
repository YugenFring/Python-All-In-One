from decorators import debug, do_twice

# Decorators being called in the order
# they're listed.
@debug
@do_twice
def say_hi(name):
    print(f"Hi {name}!")

say_hi("Fring")