from birds import Duck, Swan, Albatross

my_brids = [Duck, Swan, Albatross]

# If it walks like a duck and it quacks like a
# duck, then it must be a duck.
# Because they share the same interface, you can
# use them in a flexible manner:
for bird in my_brids:
    bird.fly()
    bird.swim()