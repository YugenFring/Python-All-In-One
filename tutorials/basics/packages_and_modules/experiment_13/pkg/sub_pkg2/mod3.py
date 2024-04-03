num = 103

def do_work():
    print(">>> [mod3] func is doing.")


# Import objects in a sibling subpackeg using
# relative import.
from ..sub_pkg1 import mod1
from .. import sub_pkg3