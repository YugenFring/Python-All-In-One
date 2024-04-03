def hello(name):
    print("Hello, " + name)


# This code will be executed
# when you import this module.
hello("Module")


# The following code will be executed
# when you run this script.
# When you import this module, the following
# code won't be executed.
# When you import his module, the `__name__`
# will be set to the module's name.
if __name__ == '__main__':
    print("Executing as standalone script")
    hello("Tom")