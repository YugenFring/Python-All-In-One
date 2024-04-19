class SampleClass:
    def __init__(self, name, age):
        # non-public attr
        self._name = name

        # name mangling
        self.__age = age
    
    def __method(self):
        """
        Name mangling is particularly useful when you want to ensure that
        a given attr or method won't get accidentally overwritten.
        """
        print(self.__age)

sample_instance = SampleClass('Fring', 25)
# See the name mangling attr
print(vars(sample_instance))

