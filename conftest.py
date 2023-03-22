import pytest


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")

@pytest.fixture(scope="module")
def set_module():
    print("Enter system")
    yield
    print("Exit system")
