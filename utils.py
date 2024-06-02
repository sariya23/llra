from datetime import datetime

from review import Review
from soup_page import SoupPage
from variables import Variables


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


def calculate_rating_of_review(review: Review) -> float:
    """
    Формула: likes/watches * 1/(curr_date - publish_date)

    likes/wathes - STR
    1/(curr_date - publish_date) - чем меньше будет отрезок времени, тем
    больше будет значение
    """
    time_delta = datetime.today().toordinal() - review.publish_datetime.toordinal()
    return ((review.likes / review.watches) * (1 / time_delta)) * 100


def create_url_to_user_reviews(user_name: str) -> str:
    return f"{Variables.BASE_URL}{user_name}{Variables.REVIEW_POSTFIX}"


def get_all_reviews_of_user(user_name: str) -> list[Review]:
    i = 2
    url = create_url_to_user_reviews(user_name)
    page = SoupPage(url)
    reviews = []
    while page.is_reviews_on_page():
        articles = page.get_all_reviews_from_page()
        reviews.extend(articles)
        page = SoupPage(f"{url}/~{i}")
        i += 1
    return reviews
