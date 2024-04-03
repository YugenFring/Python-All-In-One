# Tehre are actually 3 different ways to define a module:
# - A module can be written in Python itself.
# - A module can be written in C and loaded dynamically at run-tiume.
# - A built-in module is intrinsically contained in the interpreter.

# Moudles can be searched in a list of directories assembled from the following sources:
# - The directory from which the input script was run or the current directory if hte intereter is being run interactively
# - The list of directories contained in the `PYTHONPATH` environment variable, if it is set.
# - An installation-dependent list of directories configured at the time Python is installed.

# Import a built-in module.
import sys

print(">>> The module search path:")
# You can append the directory that you want to search at run time.
print(sys.path)
print('\n')


# Import a custom module.
import mod


print(">>> The module's location:")
print(mod.__file__)
print('\n')