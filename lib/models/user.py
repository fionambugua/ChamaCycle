import hashlib


class User:
    all = []
    
    def __init__(self, username, password = None, role = "user"):
        self.username = username
        self.role = role
        self.password_hash(password) if password else None
        User.all.append(self)
        
        
        
    @staticmethod
    def _hash(password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        return self._password_hash is not None and self._password_hash == self._password_hash(password)
    
    
        