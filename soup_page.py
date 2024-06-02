from datetime import datetime

import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

from article import Article
from locatros import Locators
from utils import convert_number_with_K_notations_to_int


class SoupPage:
    def __init__(self, url: str):
        self.__url = url
        self.__page = requests.get(url)
        self.__soup_page = BeautifulSoup(self.__page.text, "html.parser")

    def __get_all_reviews_book_titles(self) -> list[str]:
        titles = self.__soup_page.select(Locators.TITLES)
        return [title.text for title in titles]

    def __get_all_reviews_book_likes(self) -> list[int]:
        likes = self.__soup_page.select(Locators.LIKES)
        return [int(like_amount.text.strip()) for like_amount in likes]

    def __get_all_reviews_book_watches(self) -> list[int]:
        wathces = self.__soup_page.select(Locators.WATCHES)
        return [
            convert_number_with_K_notations_to_int(watch_amount.text.strip())
            for watch_amount in wathces
        ]

    def __get_all_publish_dates(self) -> list[datetime]:
        pusblish_datetimes = self.__soup_page.select(Locators.PUBLISH_DATETIME)
        return [publish_datetime.text for publish_datetime in pusblish_datetimes]

    def get_all_reviews_from_page(self) -> list[Article]:
        reviews: list[Article] = []
        likes = self.__get_all_reviews_book_likes()
        watches = self.__get_all_reviews_book_watches()
        titles = self.__get_all_reviews_book_titles()
        publish_dates = self.__get_all_publish_dates()

        for like_amount, watch_amount, title, publish_date in zip(
            likes, watches, titles, publish_dates
        ):
            reviews.append(
                Article(
                    likes=like_amount,
                    watches=watch_amount,
                    title=title,
                    publish_datetime=datetime,
                )
            )

        return reviews

    def is_reviews_on_page(self) -> bool:
        return bool(self.__get_all_reviews_book_titles())
