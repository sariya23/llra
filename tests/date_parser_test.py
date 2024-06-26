from datetime import datetime
from typing import Any

import pytest

from src.date_parser import DateParser
from src.exceptions import WrongDatetimeFormatFromApp, WrongMonthCaseFromApp


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


@pytest.mark.parametrize("wrong_ru_month_name", ("йцу", 123, (1, 2, 3)))
def test_translate_ru_month_to_en_month_neagtive(wrong_ru_month_name: Any):
    with pytest.raises(WrongMonthCaseFromApp):
        DateParser._russian_month_name_to_english_and_do_nominative_case(
            wrong_ru_month_name
        )


@pytest.mark.parametrize(
    "datetime_str,expected_object_datetime",
    [("18\xa0апреля\xa02024\xa0г. 16:52", datetime(2024, 4, 18, hour=16, minute=52))],
)
def test_parse_date_positive(datetime_str: str, expected_object_datetime: datetime):
    parser = DateParser(datetime_str)

    assert parser.parse_date() == expected_object_datetime


@pytest.mark.parametrize("wrong_datetime_format", ("18мая 2024 г. 12:45", "uewfiwef"))
def test_parse_date_negative(wrong_datetime_format: str):
    with pytest.raises(WrongDatetimeFormatFromApp):
        parser = DateParser(wrong_datetime_format)
        parser.parse_date()
