from soup_page import SoupPage

page = SoupPage("https://www.livelib.ru/reader/alexey-goloburdin/reviews")
print(*page.get_all_reviews_book_titles(), end="\t")
print(*page.get_all_reviews_book_watchs(), end="\t")
print(page.get_all_reviews_book_likes(), end="\t")

for t, w, l in zip(page.get_all_reviews_book_titles(), page.get_all_reviews_book_watchs(), page.get_all_reviews_book_likes()):
    print(f"title: {t}, watches: {w}, likes: {l}")