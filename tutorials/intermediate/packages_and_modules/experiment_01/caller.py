import mod

for i in mod.__all__:
    # Get attribute from the object.
    # Here get coresponding class in the mod.
    c = getattr(mod, i)()
    c.eat()
    c.run()