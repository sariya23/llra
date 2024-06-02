from soup_page import SoupPage
from utils import calculate_rating_of_review

BASE_URL = "https://www.livelib.ru/reader/sariya1/reviews/~1"
page = SoupPage(BASE_URL)
i = 2
reviews = []
while page.is_reviews_on_page():
    articles = page.get_all_reviews_from_page()
    reviews.extend(articles)
    page = SoupPage(f"{BASE_URL}/~{i}")
    i += 1

for i in range(len(reviews)):
    rating = calculate_rating_of_review(reviews[i])
    reviews[i].rating = rating

print(*reviews, sep="\n")
