import mod

# A module is only loaded once per interpreter
# sesson, so the statements in it will only be
# executed at the first time.
# So the following impor wont' be executed.
import mod
import mod


# You can reload this module by:
import importlib
importlib.reload(mod)