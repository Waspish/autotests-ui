import pytest


@pytest.fixture
def admin_page():
    print('fixture start')

    yield "ADMIN"
    print("clear")


@pytest.fixture
def user_page():
    print('fixture start')

    yield "USER"
    print("clear")


@pytest.fixture
def owner_page():
    print('fixture start')
    yield "OWNER"
    print("clear")


@pytest.mark.parametrize(
    "page_fixture",
    [
        "admin_page",
        "user_page",
        "owner_page",
    ],
)
def test_endpoint(
        request: pytest.FixtureRequest,
        page_fixture: str,
):
    print("Before fixture start")
    data = request.getfixturevalue(page_fixture)
    print(data)
    print("Test 1")
