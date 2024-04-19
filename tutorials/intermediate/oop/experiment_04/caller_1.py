class Record:
    """Hold a record of data."""

john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
    "is_manager": False,
}

john_record = Record()

for field, value in john.items():
    # Add field and attr to an object
    setattr(john_record, field, value)

print(john_record.name)
print(john_record.position)
print(john_record.department)
print(john_record.salary)
print(john_record.hire_date)
print(john_record.is_manager)

print()

print(john_record.__dict__)