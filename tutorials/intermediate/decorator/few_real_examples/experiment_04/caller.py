import random
from decorators import register, PLUGINS

@register
def say_hi(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    # !r flag has the effects as calling repr()
    print(f"Using {greeter!r}")
    return greeter_func(name)

print(PLUGINS)

print(randomly_greet("Alice"))

# Access to all global  variables including the plugins
print(globals())