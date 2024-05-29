from locatros import Locators
from article import Article

from bs4 import BeautifulSoup
import requests

class SoupPage:
    def __init__(self, url):
        self.__url = url
        self.__page= requests.get(url)
        self.__soup_page = BeautifulSoup(self.__page.text, "html.parser")
    
    def __get_all_reviews_book_titles(self):
        titles = self.__soup_page.select(Locators.TITLES)
        return [t.text for t in titles]

    def __get_all_reviews_book_likes(self):
        likes = self.__soup_page.select(Locators.LIKES)
        return [l.text.strip() for l in likes]

    def __get_all_reviews_book_watches(self):
        wathces = self.__soup_page.select(Locators.WATCHES)
        return [w.text.strip() for w in wathces]

    def get_all_reviews_from_page(self):
        reviews: list[Article] = []
        likes = self.__get_all_reviews_book_likes()
        watches = self.__get_all_reviews_book_watches()
        titles = self.__get_all_reviews_book_titles()

        for l, w, t in zip(likes, watches, titles):
            reviews.append(Article(title=t, watches=w, likes=l))
        
        return reviews
    
    def is_reviews_on_page(self) -> bool:
        return bool(self.__get_all_reviews_book_titles())