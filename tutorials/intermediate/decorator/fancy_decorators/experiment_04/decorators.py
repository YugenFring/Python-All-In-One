import functools

def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)
    
# Same as above,
def repeat_modified(func=None, *, num_times=2):
    if func is None:
        # Fill in some of the func's arguments and return it.
        return functools.partial(repeat, num_times=num_times)
    
    @functools.wraps(func)
    def wrapper_repeat(*args, **kwargs):
        for _ in range(num_times):
            value = func(*args, **kwargs)
        return value
    
    return wrapper_repeat