from lib.auth import register_user, login_user


def test_register_user():
    users = []

    result = register_user(
        users,
        "fiona",
        "password123",
        "member"
    )

    assert result is True
    assert len(users) == 1


def test_user_cannot_register_duplicate_username():
    users = []

    register_user(
        users,
        "fiona",
        "password123",
        "member"
    )

    result = register_user(
        users,
        "fiona",
        "differentpassword",
        "member"
    )

    assert result is False


def test_login_with_correct_password():
    users = []

    register_user(
        users,
        "fiona",
        "password123",
        "member"
    )

    result = login_user(
        users,
        "fiona",
        "password123"
    )

    assert result is not None


def test_login_with_wrong_password_fails():
    users = []

    register_user(
        users,
        "fiona",
        "password123",
        "member"
    )

    result = login_user(
        users,
        "fiona",
        "wrongpassword"
    )

    assert result is None


def test_password_is_hashed():
    users = []

    register_user(
        users,
        "fiona",
        "password123",
        "member"
    )

    assert users[0]["password"] != "password123"