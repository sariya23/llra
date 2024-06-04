from datetime import datetime


class DateParser:
    MONTH_POSITION = 1
    SPECIAL_DELIMETER_DATE = "\xa0"
    DATETIME_PATTERN = "%d %B %Y г. %H:%M"

    def __init__(self, datetime_: str) -> None:
        self.datetime_ = datetime_

    @staticmethod
    def _russian_month_name_to_english_and_do_genetive_case(
        russian_month_name: str,
    ) -> str:
        """
        Переводит название месяца с русского языка на английский и переводит
        первую букву месяца в верхний регистр.
        """
        ru_en_month = {
            "января": "January",
            "февраля": "February",
            "марта": "March",
            "апреля": "April",
            "мая": "May",
            "июня": "June",
            "июля": "July",
            "августа": "August",
            "сентября": "September",
            "октября": "October",
            "ноября": "November",
            "декабря": "December",
        }
        return ru_en_month[russian_month_name]

    def __split_date(self, datetime_: str) -> list[str]:
        """
        Разбивает дату-строку на спиосок.
        """
        return datetime_.split(self.SPECIAL_DELIMETER_DATE)

    def parse_date(self) -> datetime:
        splited_date: list[str] = self.__split_date(self.datetime_)
        ru_month_name = splited_date[self.MONTH_POSITION]
        en_month_name = self._russian_month_name_to_english_and_do_genetive_case(
            ru_month_name
        )
        splited_date[self.MONTH_POSITION] = en_month_name
        return datetime.strptime(" ".join(splited_date), self.DATETIME_PATTERN)
