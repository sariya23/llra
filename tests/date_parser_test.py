import pytest

from date_parser import DateParser


@pytest.mark.parametrize(
    "ru_month_name,expected_en_name",
    [
        ("января", "January"),
        ("февраля", "February"),
        ("марта", "March"),
        ("апреля", "April"),
        ("мая", "May"),
        ("июня", "June"),
        ("июля", "July"),
        ("августа", "August"),
        ("сентября", "September"),
        ("октября", "October"),
        ("ноября", "November"),
        ("декабря", "December"),
    ],
)
def test_translate_ru_month_to_en_month_positive(
    ru_month_name: str, expected_en_name: str
):
    assert (
        DateParser._russian_month_name_to_english_and_do_nominative_case(ru_month_name)
        == expected_en_name
    )
