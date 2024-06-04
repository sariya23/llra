import pytest

from src.soup_page import SoupPage


@pytest.mark.parametrize(
    "value,expected_value", [("123", 123), ("1K", 1000), ("10K", 10_000), ("999", 999)]
)
def test_convert_number_with_K_notations_to_int_positive(
    value: str, expected_value: int
):
    assert SoupPage.convert_number_with_K_notations_to_int(value) == expected_value
