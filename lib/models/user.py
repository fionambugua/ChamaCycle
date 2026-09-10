import hashlib


class User:
    all = []
    
    def __init__(self, username, password = None, role = "user"):
        self.username = username
        self.role = role
        self.password_hash(password) if password else None
        User.all.append(self)
        