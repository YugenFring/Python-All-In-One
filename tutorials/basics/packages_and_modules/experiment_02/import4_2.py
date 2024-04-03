try:
    import mod
    mod.hello()
except ImportError:
    print("Module not found.")