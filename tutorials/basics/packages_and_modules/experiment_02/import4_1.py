def test():
    # `import *` is not allowed.
    from mod import num
    print(num)

test()