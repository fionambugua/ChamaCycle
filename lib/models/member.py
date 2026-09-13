from lib.models.user import User

class Member(User):
    def __init__(self, name, password=None):
        super().__init__(username=name, password=password, role="member")
        self.chamas = []