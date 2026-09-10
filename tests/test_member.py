import pytest
from lib.models.member import Member


def test_member_has_name():
    member = Member("Fiona")

    assert member.name == "Fiona"


def test_member_starts_with_empty_chamas():
    member = Member("Fiona")

    assert member.chamas == []


def test_member_can_join_multiple_chamas():
    member = Member("Fiona")

    chama1 = "Nairobi Women Chama"
    chama2 = "Friends Chama"

    member.chamas.append(chama1)
    member.chamas.append(chama2)

    assert len(member.chamas) == 2
    assert chama1 in member.chamas
    assert chama2 in member.chamas