import pytest
from lib.models.contribution import Contribution

class FakeMember:
    def __init__(self, name):
        self.name = name

class FakeChama:
    def __init__(self, name):
        self.name = name

@pytest.fixture(autouse=True)
def reset_contributions():
    Contribution.all_contributions = []
    yield

def test_contribution_store_attribute():
    member = FakeMember("Asha")
    chama = FakeChama("Umoja")

    contribution = Contribution(member, chama, 500, "January")

    assert contribution.member == member
    assert contribution.chama == chama
    assert contribution.amount == 500
    assert contribution.month == "January"

def test_new_contribution_added_to_all_contributions():
    member = FakeMember("Asha")
    chama = FakeChama("Umoja")

    contribution = Contribution(member, chama, 500, "January")

    assert contribution in Contribution.all_contributions
    assert len(Contribution.all_contributions) == 1

def test_contribution_rejects_negative_amount():
    member = FakeMember("Asha")
    chama = FakeChama("Umoja")
 
    with pytest.raises(ValueError):
        Contribution(member, chama, -100, "January")

def test_contribution_rejects_zero_amount():
    member = FakeMember("Asha")
    chama = FakeChama("Umoja")
 
    with pytest.raises(ValueError):
        Contribution(member, chama, 0, "January")
    