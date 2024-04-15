from decorators import count_calls

@count_calls
def say_hi():
    print("Hi")

say_hi()
say_hi()
say_hi()

print(say_hi.num_calls)