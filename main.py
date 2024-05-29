from soup_page import SoupPage

BASE_URL = "https://www.livelib.ru/reader/sariya1/reviews"
page = SoupPage(BASE_URL)
i = 1

while page.get_all_reviews_book_likes():
    titles = page.get_all_reviews_book_titles()
    wathes = page.get_all_reviews_book_watchs()
    likes = page.get_all_reviews_book_likes()

    for t, w, l in zip(titles, wathes, likes):
        print(f"title: {t}, watches: {w}, likes: {l}")
    
    page = SoupPage(f"{BASE_URL}/~{i}")
    i += 1