num = 106

def do_work():
    print(">>> [mod6] func is doing.")

# Import objects in the same package using
# relative import.
from .mod5 import do_work as my_do_work