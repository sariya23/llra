from utils import get_all_reviews_of_user

reviews = get_all_reviews_of_user("sariya1")
print(
    *sorted(reviews, key=lambda r: r.calculate_rating_of_review(), reverse=True),
    sep="\n"
)
