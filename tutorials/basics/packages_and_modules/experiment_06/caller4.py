# In this experiment, import this packge will
# not place any of the moduels in to the local
# namespace.
import pkg


try:
    print(pkg.mod1)
except AttributeError:
    print("Can't find mod1")