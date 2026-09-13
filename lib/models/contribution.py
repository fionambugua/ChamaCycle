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

    @staticmethod
    def _validate_month(month):
        if month not in MONTH_ORDER:
            raise ValueError(
                f"'{month}' is not a valid month name. "
                f"Expected one of: {', '.join(MONTH_ORDER)}."
            )

    @classmethod
    def _check_duplicate(cls, member, chama, month):
        duplicate_exists = any(
            c.member == member and c.chama == chama and c.month == month
            for c in cls.all_contributions
        )
        if duplicate_exists:
            name = getattr(member, "name", "This member")
            raise ValueError(
                f"{name} already has a recorded contribution for {month}."
            )

    @classmethod
    def find_by_member(cls, member):
        matches = [c for c in cls.all_contributions if c.member == member]
        return sorted(matches, key=lambda c: MONTH_ORDER.index(c.month))

    @classmethod
    def total_for_chama(cls, chama):
        return sum(
            c.amount for c in cls.all_contributions if c.chama == chama
        )

    @classmethod
    def members_who_paid(cls, chama, month):
        return {
            c.member for c in cls.all_contributions
            if c.chama == chama and c.month == month
        }
 
    def __repr__(self):
        member_name = getattr(self.member, "name", self.member)
        return f"<Contribution {member_name} - {self.amount} ({self.month})>"