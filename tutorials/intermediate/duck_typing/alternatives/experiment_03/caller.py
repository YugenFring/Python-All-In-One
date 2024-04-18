from birds import Duck, Pigeon

my_birds = [Duck(), Pigeon()]

for bird in my_birds:
    # Check whether an object comes from a
    # given class.
    if isinstance(bird, Duck):
        bird.swim()

for bird in my_birds:
    # Check whether an object has a specific
    # method or attribute.
    if hasattr(bird, 'swim'):
        bird.swim()