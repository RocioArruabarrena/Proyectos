from user import User

class UserBuilder:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.age = None
        self.address = None

    def with_age(self, age):
        self.age = age
        return self

    def with_address(self, address):
        self.address = address
        return self

    def build(self):
        return User(self.username, self.email, self.age, self.address)
