from src.review import Review
from src.soup_page import SoupPage
from src.variables import Variables


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
