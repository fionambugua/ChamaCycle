import pytest
from lib.models.contribution import contribution

class FakeMember:
    def __init__(self, name):
        self.name = name

class FakeChama:
    def __init__(self, name):
        self.name = name