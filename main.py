from soup_page import SoupPage

BASE_URL = "https://www.livelib.ru/reader/sariya1/reviews/~1"
page = SoupPage(BASE_URL)
i = 2

while page.get_all_reviews_book_likes():
    articles = page.get_all_reviews_from_page()
    print(*articles, sep='\n')
    page = SoupPage(f"{BASE_URL}/~{i}")
    i += 1