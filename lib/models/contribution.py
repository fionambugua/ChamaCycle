MONTH_ORDER = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

class Contribution:
    all_contributions = []
 
    def __init__(self, member, chama, amount, month):
        self._validate_amount(amount)
        self._validate_month(month)
        self._check_duplicate(member, chama, month)
 
        self.member = member
        self.chama = chama
        self.amount = amount
        self.month = month
 
        Contribution.all_contributions.append(self)

    @staticmethod
    def _validate_amount(amount):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise ValueError("Contribution amount must be a number.")
        if amount <= 0:
            raise ValueError("Contribution amount must be positive.")