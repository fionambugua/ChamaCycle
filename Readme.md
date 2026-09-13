# ChamaCycle

**Know your cycle. Trust your circle.**

A Python CLI-based chama (informal savings group) management system —
one shared, trustworthy record of contributions, balances, payout
order, and member accounts, replacing the notebook, spreadsheet, and
"did I pay this month?" WhatsApp messages most chamas rely on today.

---

## What it does

- Register and log in as a **Member** or **Admin** (treasurer)
- Add a member to a chama
- Record a contribution (amount + month), with validation against
  negative/zero/non-numeric amounts and duplicate entries
- View a member's contribution history, sorted chronologically
- View a chama's total pool balance
- View who has/hasn't paid in a given month
- View the next payout recipient and a member's position in the
  rotation
- View every chama a member belongs to

**Out of scope for now:** loans, automated payments / M-Pesa STK push,
SQL/database persistence (everything is in-memory for the current
milestone).

---

## Setup

```bash
git clone <repo-url>
cd ChamaCycle-development
pipenv install
pipenv shell
```

## Running the tests

```bash
pytest
```

A `pytest.ini` in the project root sets `pythonpath = .`, so plain
`pytest` resolves `lib` imports correctly regardless of which folder
you run it from. To run a single file:

```bash
pytest tests/test_member.py -v
```

## Running the CLI

```bash
python -m lib.cli
```

*(CLI entry point is still under construction — see Project Status
below.)*

---

## Project Structure

```
ChamaCycle-development/
├── Pipfile
├── Readme.md
├── pytest.ini
├── lib/
│   ├── cli.py              # menu loop — entry point, calls into models only
│   ├── auth.py              # register_user() / login_user() — session-level auth
│   ├── helpers.py           # input validation, formatting helpers
│   ├── debug.py             # drops into ipdb with sample objects
│   └── models/
│       ├── __init__.py
│       ├── user.py           # User — base class: username, password hash, role
│       ├── member.py         # Member(User) — chama membership, name alias
│       ├── admin.py          # Admin(User) — treasurer account
│       ├── contribution.py   # Contribution — validated record + query methods
│       └── chama.py          # Chama — members, rotation logic
└── tests/
    ├── test_user.py
    ├── test_member.py
    ├── test_auth.py
    ├── test_contribution.py
    └── test_chama.py
```

---

## Architecture notes

- **`User` is the base class** for both `Member` and `Admin`. It owns
  `username`, `role`, and password hashing (SHA-256 — adequate for
  this project, not production-grade since it isn't salted). Passwords
  are never stored or compared in plaintext; use `check_password()`
  to verify a login attempt.
- **`lib/auth.py` is intentionally decoupled** from the `User` model
  classes — `register_user()` / `login_user()` operate on a plain list
  of dicts so the CLI can manage a lightweight session without needing
  the full object graph. This may get unified with `User` later; open
  question for the team.
- **`Member.chamas` is a plain list.** `Member` no longer has a
  `join_chama()` method — `Chama.add_member()` is the single place
  responsible for updating both sides of the Member <-> Chama
  relationship. Anyone touching `chama.py` needs to remember to append
  to `member.chamas` there, or Story 7 (view all chamas a member
  belongs to) will silently return incomplete data.
- **Authentication was not part of the original project scope
  document.** It's been added as a team-agreed extension covering
  login/registration for members and admins; flagging here so it's
  traceable for anyone reviewing against the original spec.

---

## Project Status

| Area | Status |
|---|---|
| `User` / `Member` / `Admin` | Done, tested |
| `lib/auth.py` (register/login) | Done, tested |
| `Contribution` | Done, tested |
| `Chama` (rotation logic) | In progress |
| `cli.py` (menu loop) | Not started |
| `helpers.py` | Not started |
| `debug.py` | Not started |

---

## Ground rules

- **Exact naming matters** — CodeGrade autograding requires exact
  method names. Agree on shared method names (e.g. `add_member`,
  `record_contribution`) before writing code that depends on them.
- **Both sides of a relationship update together** — see the
  `Chama.add_member()` note above.
- **No shared mutable defaults** — a class-level list like
  `all = []` is fine as a registry, but instance attributes
  (`self.chamas`, `self.members`) must always be initialized fresh
  inside `__init__`.
- **`cli.py` stays thin** — all logic lives in the model classes; the
  CLI only calls methods and prints results.