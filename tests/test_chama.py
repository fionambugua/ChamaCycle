
from lib.models.member import Member
from lib.models.chama import Chama


def test_payout_rotation():
    chama = Chama("Harambee Chama")

    benard = Member("Benard")
    john = Member("John")
    mary = Member("Mary")

    chama.add_member(benard)
    chama.add_member(john)
    chama.add_member(mary)

    assert chama.next_payout_recipient() == benard

    chama.mark_payout(benard)

    assert chama.next_payout_recipient() == john

    chama.mark_payout(john)

    assert chama.next_payout_recipient() == mary


def test_payout_position():
    chama = Chama("Harambee Chama")

    benard = Member("Benard")
    john = Member("John")
    mary = Member("Mary")

    chama.add_member(benard)
    chama.add_member(john)
    chama.add_member(mary)

    assert chama.payout_position(benard) == 1
    assert chama.payout_position(john) == 2
    assert chama.payout_position(mary) == 3


def test_no_next_payout_when_all_members_are_paid():
    chama = Chama("Harambee Chama")

    benard = Member("Benard")
    john = Member("John")

    chama.add_member(benard)
    chama.add_member(john)

    chama.mark_payout(benard)
    chama.mark_payout(john)

    assert chama.next_payout_recipient() is None

