class ObjectCounter:
    # Class Attribute
    num_instances = 0
    def __init__(self):
        # Instance Attribute
        self.num_instances += 1

ObjectCounter()
ObjectCounter()
ObjectCounter()
ObjectCounter()
one_instance = ObjectCounter()

print(ObjectCounter.num_instances)
print(one_instance.num_instances)