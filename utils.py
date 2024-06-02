from datetime import datetime

from article import Article


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


def calculate_rating_of_review(review: Article) -> float:
    """
    Формула: likes/watches * 1/(curr_date - publish_date)

    likes/wathes - STR
    1/(curr_date - publish_date) - чем меньше будет отрезок времени, тем
    больше будет значение
    """
    time_delta = datetime.today().toordinal() - review.publish_datetime.toordinal()
    return ((review.likes / review.watches) * (1 / time_delta)) * 100
