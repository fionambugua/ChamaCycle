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