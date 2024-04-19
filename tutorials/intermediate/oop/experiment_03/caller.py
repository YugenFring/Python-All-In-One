class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    def method(self):
        print(f'Class attr: {self.class_attr}')
        print(f'Instance attr: {self.instance_attr}')

print(SampleClass.class_attr)
print(SampleClass.__dict__)
print(SampleClass.__dict__['class_attr'])

print()

sample_instance = SampleClass('Fring')
print(sample_instance.instance_attr)
print(sample_instance.__dict__)
print(sample_instance.__dict__['instance_attr'])