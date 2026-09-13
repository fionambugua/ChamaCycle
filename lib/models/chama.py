class Chama:
    def _init_(self, name):
        self.name = name
        self.members = []
        self.contributions = []
        self.payout_order = []
        self.paid_out_members = []

    def add_member(self, member):
        """Add a member and place them in the payout rotation."""
        if member not in self.members:
            self.members.append(member)

            # Keep the Member <-> Chama relationship connected
            if self not in member.chamas:
                member.chamas.append(self)

            # Add new member to the payout rotation
            self.payout_order.append(member)

    def add_contribution(self, contribution):
        """Add a contribution to the chama."""
        self.contributions.append(contribution)

    def pool_balance(self):
        """Calculate the total amount contributed."""
        return sum(
            contribution.amount
            for contribution in self.contributions
        )

    def members_not_paid(self, month):
        """Return members who have not contributed during a given month."""
        paid_members = [
            contribution.member
            for contribution in self.contributions
            if contribution.month == month
        ]

        return [
            member
            for member in self.members
            if member not in paid_members
        ]

    def next_payout_recipient(self):
        """Return the next member who should receive the payout."""
        for member in self.payout_order:
            if member not in self.paid_out_members:
                return member

        return None

    def payout_position(self, member):
        """Return the member's position in the payout rotation."""
        if member in self.payout_order:
            return self.payout_order.index(member) + 1

        return None

    def mark_payout(self, member):
        """Mark a member as having received their payout."""
        if member in self.payout_order:
            if member not in self.paid_out_members:
                self.paid_out_members.append(member)

    def reset_payout_cycle(self):
        """Start a new payout cycle."""
        self.paid_out_members.clear()
