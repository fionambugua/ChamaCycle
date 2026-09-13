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

def test_contribution_rejects_non_numeric_amount():
    member = FakeMember("Asha")
    chama = FakeChama("Umoja")
 
    with pytest.raises(ValueError):
        Contribution(member, chama, "five hundred", "January")

def test_duplicate_member_and_month_is_flagged():
    member = FakeMember("Asha")
    chama = FakeChama("Umoja")
 
    Contribution(member, chama, 500, "January")

    with pytest.raises(ValueError):
        Contribution(member, chama, 500, "January")

def test_find_by_member_returns_only_that_members_contributions():
    asha = FakeMember("Asha")
    jeff = FakeMember("Jeff")
    chama = FakeChama("Umoja")
 
    Contribution(asha, chama, 500, "January")
    Contribution(jeff, chama, 300, "January")
    Contribution(asha, chama, 500, "February")
 
    results = Contribution.find_by_member(asha)
 
    assert len(results) == 2
    assert all(c.member == asha for c in results)

def test_find_by_member_returns_empty_list_when_none_exist():
    asha = FakeMember("Asha")
 
    results = Contribution.find_by_member(asha)
 
    assert results == []
 
 
def test_find_by_member_sorted_by_month_ascending():
    asha = FakeMember("Asha")
    chama = FakeChama("Umoja")

    Contribution(asha, chama, 500, "March")
    Contribution(asha, chama, 500, "January")
    Contribution(asha, chama, 500, "February")
 
    results = Contribution.find_by_member(asha)
    months = [c.month for c in results]
 
    assert months == ["January", "February", "March"]

def test_total_for_chama_sums_all_contributions():
    asha = FakeMember("Asha")
    jeff = FakeMember("Jeff")
    chama = FakeChama("Umoja")
 
    Contribution(asha, chama, 500, "January")
    Contribution(jeff, chama, 300, "January")
 
    total = Contribution.total_for_chama(chama)
 
    assert total == 800

def test_total_for_chama_is_zero_with_no_contributions():
    chama = FakeChama("Umoja")
 
    total = Contribution.total_for_chama(chama)
 
    assert total == 0

def test_total_for_chama_ignores_other_chamas():
    asha = FakeMember("Asha")
    umoja = FakeChama("Umoja")
    tuungane = FakeChama("Tuungane")
 
    Contribution(asha, umoja, 500, "January")
    Contribution(asha, tuungane, 1000, "January")
 
    assert Contribution.total_for_chama(umoja) == 500
    assert Contribution.total_for_chama(tuungane) == 1000

 
    