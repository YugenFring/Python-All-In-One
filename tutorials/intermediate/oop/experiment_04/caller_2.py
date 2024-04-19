class User:
    pass

john = User()
john.name = 'John'
john.job = 'Data Engineer'

print(john.__dict__)

print()

def __init__(self, name, job):
    self.name = name
    self.job = job

User.__init__ = __init__

linda = User('Linda', 'Team Lead')
print(linda.__dict__)