from lib.models.user import User

class Admin(User):
    def __init__(self, username, password=None):
        super().__init__(username=username, password=password, role="admin")
        
    
    