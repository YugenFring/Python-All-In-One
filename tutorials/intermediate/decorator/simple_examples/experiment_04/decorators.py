# The decorated function is used as `func` arg.
# `wrapper` func is used to replace the decorated
# func, so it takes the arguments.
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper