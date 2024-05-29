from soup_page import SoupPage

page = SoupPage("https://www.livelib.ru/reader/alexey-goloburdin/reviews/~5")


for t, w, lk in zip(page.get_all_reviews_book_titles(), page.get_all_reviews_book_watchs(), page.get_all_reviews_book_likes()):
    print(f"title: {t}, watches: {w}, likes: {lk}")
print(page.get_all_reviews_book_titles())