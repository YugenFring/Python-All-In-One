from decorators import cache, count_calls

# See the difference without `@cache`
@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(10))
print(fibonacci(8))