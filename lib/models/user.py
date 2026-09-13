import hashlib


class User:
    """
    Base class for anyone who can log into ChamaCycle (Member or Admin).
    Handles identity (username, role) and password hashing.
    """

    all = []

    def __init__(self, username, password=None, role="user"):
        self.username = username
        self.role = role
        self._password_hash = self._hash(password) if password else None
        User.all.append(self)

    @staticmethod
    def _hash(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """Verify a plaintext password against the stored hash."""
        return self._password_hash is not None and self._password_hash == self._hash(password)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.username} ({self.role})>"