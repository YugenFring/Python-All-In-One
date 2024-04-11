import functools

def do_twice(func):
    # Give the decorated func name to
    # the wrapper.
    # See what will happen if this doesn't
    # applied.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        # Return values from decorator
        return func(*args, **kwargs)
    return wrapper