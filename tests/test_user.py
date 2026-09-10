from lib.models.user import User
from lib.models.member import Member
from lib.models.admin import Admin


def test_user_has_username():
    user = User("fiona", "password123", "member")

    assert user.username == "fiona"


def test_user_has_role():
    user = User("fiona", "password123", "member")

    assert user.role == "member"


def test_member_inherits_from_user():
    member = Member("fiona", "password123")

    assert isinstance(member, User)


def test_admin_inherits_from_user():
    admin = Admin("treasurer", "password123")

    assert isinstance(admin, User)