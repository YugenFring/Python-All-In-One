import time

# This is a wrong example using data descriptor (containing `__set__()`
# or `__delete__()`).
# See 'experiemnt_03 -> caller_02.py' for the answer.
class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]
    
    # Just add this method.
    def __set__(self, obj, value):
        pass

class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return 42
   
my_deep_thought = DeepThought()

print(my_deep_thought.meaning_of_life)
print(my_deep_thought.meaning_of_life)
print(my_deep_thought.meaning_of_life)