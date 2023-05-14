import pytest

@pytest.fixture(scope="module")
def set_up():
    print("\nSTART TEST")
    yield
    print("\nFINISH TEST")

