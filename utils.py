def convert_number_with_K_notations_to_int(amount_of_watches: str) -> int:
    """
    Переводит запись вида nK в целое число n.

    Например:
    >>> convert_number_with_K_notations_to_int("2K")
    >>> 2000

    !K Латинская!
    """
    if "K" in amount_of_watches:
        k_index = amount_of_watches.find("K")
        number = int(amount_of_watches[:k_index])
        return number * 1000

    return int(amount_of_watches)


def russian_month_name_to_english_with_title(russian_month_name: str) -> str:
    """
    Переводит название месяца с русского языка на английский и переводит
    первую букву месяца в верхний регистр.
    """
    ru_en_month = {
        "января": "Junuary",
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
