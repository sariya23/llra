from locatros import Locators

from bs4 import BeautifulSoup
import requests

class SoupPage:
    def __init__(self, url):
        self.__url = url
        self.__page= requests.get(url)
        self.__soup_page = BeautifulSoup(self.__page.text, "html.parser")
    
    def get_all_reviews_book_titles(self):
        titles = self.__soup_page.select(Locators.TITLES)
        return [t.text for t in titles]

    def get_all_reviews_book_likes(self):
        likes = self.__soup_page.select(Locators.LIKES)
        return [l.text.strip() for l in likes]

    def get_all_reviews_book_watchs(self):
        wathces = self.__soup_page.select(Locators.WATCHES)
        return [w.text.strip() for w in wathces]