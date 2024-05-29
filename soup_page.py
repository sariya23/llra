from bs4 import BeautifulSoup
import requests

class SoupPage:
    def __init__(self, url):
        self.__url = url
        self.__page= requests.get(url)
        self.__soup_page = BeautifulSoup(self.__page.text, "html.parser")
    
    def get_all_reviews_book_titles(self):
        titles = []
        for i in self.__soup_page.select("article"):
            titles.append(i.select('div.lenta-card > div.lenta-card-book > div.lenta-card-book__wrapper > a')[0].text.strip())
        return titles

    def get_all_reviews_book_likes(self):
        likes = []
        for i in self.__soup_page.select("article"):
            likes.append(i.select('div.review-card__footer > div.sab > div[data-type="vote"] > a > span')[0].text.strip())
        return likes

    def get_all_reviews_book_watchs(self):
        wathces = []
        for i in self.__soup_page.select("article"):
            wathces.append(i.select("div.lenta-card > .lenta-card__details > p:nth-child(2)")[0].text.strip())
        return wathces