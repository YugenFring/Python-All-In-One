def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        # Return values from decorator
        return func(*args, **kwargs)
    return wrapper