from soup_page import SoupPage


page = SoupPage(f"https://www.livelib.ru/reader/alexey-goloburdin/reviews")
i = 1

while page.get_all_reviews_book_likes():
    titles = page.get_all_reviews_book_titles()
    wathes = page.get_all_reviews_book_watchs()
    likes = page.get_all_reviews_book_likes()

    for t, w, l in zip(titles, wathes, likes):
        print(f"title: {t}, watches: {w}, likes: {l}")
    
    page = SoupPage(f"https://www.livelib.ru/reader/alexey-goloburdin/reviews~{i}")
    i += 1