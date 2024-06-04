import pytest

from utils import create_url_to_user_reviews


@pytest.mark.parametrize(
    "user_name,expected_url",
    [("ABOBA", "https://www.livelib.ru/reader/ABOBA/reviews/~1")],
)
def test_create_url_positive(user_name: str, expected_url: str):
    assert create_url_to_user_reviews(user_name) == expected_url
