class User:
    def __init__(self, username, email, age=None, address=None):
        self.username = username
        self.email = email
        self.age = age
        self.address = address

    def __str__(self):
        return f"User(username={self.username}, email={self.email}, age={self.age}, address={self.address})"
