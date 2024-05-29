from bs4 import BeautifulSoup
import requests

class SoupPage:
    def __init__(self, url):
        self.__url = url
        self.__page= requests.get(url)
        self.__soup_page = BeautifulSoup(self.__page.text, "html.parser")
    
    def get_all_reviews_book_titles(self):
        titles = self.__soup_page.select("div.lenta-card > div.lenta-card-book > div.lenta-card-book__wrapper > a")
        return [t.text for t in titles]

    def get_all_reviews_book_likes(self):
        likes = self.__soup_page.select('div.review-card__footer > div.sab > div[data-type="vote"] > a > span')
        return [l.text.strip() for l in likes]

    def get_all_reviews_book_watchs(self):
        wathces = self.__soup_page.select("div.lenta-card > .lenta-card__details > p:nth-child(2)")
        return [w.text.strip() for w in wathces]