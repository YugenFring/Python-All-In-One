import time

# Evaluate the method just once when it's first executed and
# cache the resulting value so that you can get it in no time.
class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return 42
   
my_deep_thought = DeepThought()

print(my_deep_thought.meaning_of_life)
print(my_deep_thought.meaning_of_life)
print(my_deep_thought.meaning_of_life)