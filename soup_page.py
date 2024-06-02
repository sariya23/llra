from datetime import datetime

import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore

from date_parser import DateParser
from locatros import Locators
from review import Review


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
            self.convert_number_with_K_notations_to_int(watch_amount.text.strip())
            for watch_amount in wathces
        ]

    def __get_all_publish_dates(self) -> list[datetime]:
        pusblish_datetimes_tags = self.__soup_page.select(Locators.PUBLISH_DATETIME)
        pusblish_datetimes = [
            publish_dt_tag.text for publish_dt_tag in pusblish_datetimes_tags
        ]
        for i in range(len(pusblish_datetimes)):
            date_parser = DateParser(pusblish_datetimes[i])
            pusblish_datetimes[i] = date_parser.parse_date()
        return pusblish_datetimes

    def get_all_reviews_from_page(self) -> list[Review]:
        reviews: list[Review] = []
        likes = self.__get_all_reviews_book_likes()
        watches = self.__get_all_reviews_book_watches()
        titles = self.__get_all_reviews_book_titles()
        publish_datetimes = self.__get_all_publish_dates()
        for like_amount, watch_amount, title, publish_datetime in zip(
            likes, watches, titles, publish_datetimes
        ):
            reviews.append(
                Review(
                    likes=like_amount,
                    watches=watch_amount,
                    title=title,
                    publish_datetime=publish_datetime,
                )
            )

        return reviews

    def is_reviews_on_page(self) -> bool:
        return bool(self.__get_all_reviews_book_titles())

    @staticmethod
    def convert_number_with_K_notations_to_int(amount_of_watches: str) -> int:
        """
        Переводит запись вида nK в целое число n.

        Например:
        >>> convert_number_with_K_notations_to_int("2K")
        >>> 2000

        !K Латинская!
        """
        if "K" in amount_of_watches:
            k_index = amount_of_watches.find("K")
            number = int(amount_of_watches[:k_index])
            return number * 1000

        return int(amount_of_watches)
