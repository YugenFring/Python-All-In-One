print(">>> Return a list of defined names in the namespace:")
print(dir())
print("\n")


print(">>> Add a object in the namespace:")
num = 10001
print(dir())
print("\n")


print(">>> Import a module into the namespace:")
import mod
print(dir())
print("\n")


# List the names defined in a module.
print(">>> List the names defined in a module:")
print(dir(mod))
print("\n")