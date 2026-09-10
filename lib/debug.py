from lib.models.member import Member
from lib.models.chama import Chama

chama = Chama("Harambee Chama")

benard = Member("Benard")
john = Member("John")
mary = Member("Mary")

chama.add_member(benard)
chama.add_member(john)
chama.add_member(mary)

print("Payout order:")

for position, member in enumerate(chama.payout_order, start=1):
    print(position, member.name)
print("Next payout:", chama.next_payout_recipient().name)
