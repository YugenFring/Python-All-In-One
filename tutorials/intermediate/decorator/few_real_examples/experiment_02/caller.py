from decorators import debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Hi {name}!"
    else:
        return f"Hi {name}! {age} already."

make_greeting("Fring")

make_greeting("Rodman", age=25)