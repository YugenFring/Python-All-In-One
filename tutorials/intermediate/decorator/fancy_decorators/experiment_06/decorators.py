import functools

class CountCalls:
    def __init__(self, func):
        # Used in place of `functools.wrapper()`.
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    # `__call__` method is executed each time you try to call
    # an instance of the class.
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}()")
        return self.func(*args, **kwargs)   