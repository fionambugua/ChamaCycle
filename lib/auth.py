import hashlib

def _hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(users, username, password, role):
    if any(u["username"] == username for u in users):
        return False
    
    users.append({
        "username": username,
        "password": _hash_password(password),
        "role": role,
    })
    return True