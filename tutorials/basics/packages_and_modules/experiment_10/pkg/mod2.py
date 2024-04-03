num = 102

module_name = "mod2"

def do_work():
    print(">>> [mod2] func is doing.")

def say_hello():
    print(">>> [mod2] hello world.")


# Define the object name is imported when
# `form <module_name> import *` is encountered.
__all__ = ["num", "say_hello"]