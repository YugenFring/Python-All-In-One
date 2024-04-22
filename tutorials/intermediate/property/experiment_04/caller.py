import hashlib
import os


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        # Make attr `password` write-only.
        raise AttributeError('Password is write-only!')
    
    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            'sha256', plaintext.encode('utf-8'), salt, 100_000
        )


john = User('John', 'asdf1234')
print(john._hashed_password)
print()

print(john.password)