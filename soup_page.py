import requests
from bs4 import BeautifulSoup

from article import Article
from locatros import Locators


class SoupPage:
    def __init__(self, url):
        self.__url = url
        self.__page = requests.get(url)
        self.__soup_page = BeautifulSoup(self.__page.text, "html.parser")

    def __get_all_reviews_book_titles(self):
        titles = self.__soup_page.select(Locators.TITLES)
        return [title.text for title in titles]

    def __get_all_reviews_book_likes(self):
        likes = self.__soup_page.select(Locators.LIKES)
        return [like_amount.text.strip() for like_amount in likes]

    def __get_all_reviews_book_watches(self):
        wathces = self.__soup_page.select(Locators.WATCHES)
        return [watch_amount.text.strip() for watch_amount in wathces]

    def get_all_reviews_from_page(self):
        reviews: list[Article] = []
        likes = self.__get_all_reviews_book_likes()
        watches = self.__get_all_reviews_book_watches()
        titles = self.__get_all_reviews_book_titles()

        for like_amount, watch_amount, title in zip(likes, watches, titles):
            reviews.append(
                Article(likes=like_amount, watches=watch_amount, title=title)
            )

        return reviews

    def is_reviews_on_page(self) -> bool:
        return bool(self.__get_all_reviews_book_titles())
