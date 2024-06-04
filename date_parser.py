from datetime import datetime

from exceptions import WrongDatetimeFormatFromApp, WrongMonthCaseFromApp


class DateParser:
    """
    Класс используется для преобразования даты из строки в объект datetime.

    Формат даты и времени с livelib: day\xa0ru_month_name\xa0year\xa0г.\xa0hours:minutes
    """

    MONTH_POSITION = 1
    SPECIAL_DELIMETER_DATE = "\xa0"
    DATETIME_PATTERN = "%d %B %Y г. %H:%M"

    def __init__(self, datetime_: str) -> None:
        self.datetime_ = datetime_

    @staticmethod
    def _russian_month_name_to_english_and_do_nominative_case(
        russian_month_name: str,
    ) -> str:
        """
        Перводит название месяца с русского на английский и меняет его падеж с
        родительного на именительный. Также первая буква становится заглавной.
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
        try:
            return ru_en_month[russian_month_name]
        except KeyError:
            raise WrongMonthCaseFromApp(
                f"Month case changed in app. Cant parse {russian_month_name}"
            )

    def __split_date(self, datetime_: str) -> list[str]:
        """
        Разбивает дату-строку на спиосок.
        """
        return datetime_.split(self.SPECIAL_DELIMETER_DATE)

    def __get_month(self, datetime_list: list[str]) -> str:
        try:
            return datetime_list[self.MONTH_POSITION]
        except IndexError:
            raise WrongDatetimeFormatFromApp(
                f"Datetime format changed in app. Cant parse {datetime_list}"
            )

    def parse_date(self) -> datetime:
        splited_date: list[str] = self.__split_date(self.datetime_)
        ru_month_name = self.__get_month(splited_date)
        en_month_name = self._russian_month_name_to_english_and_do_nominative_case(
            ru_month_name
        )
        splited_date[self.MONTH_POSITION] = en_month_name
        return datetime.strptime(" ".join(splited_date), self.DATETIME_PATTERN)
