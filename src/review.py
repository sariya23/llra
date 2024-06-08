from datetime import datetime
from math import log


class Review:
    def __init__(
        self, title: str, likes: int, watches: int, publish_datetime: datetime
    ):
        self.title = title
        self.likes = likes
        self.watches = watches
        self.publish_datetime = publish_datetime

    def __repr__(self):
        return f"Review({self.title}, {self.likes}, {self.watches}, {self.publish_datetime}, {self.calculate_rating_of_review()})"

    def __str__(self):
        return f"Название книг: {self.title}"

    def calculate_rating_of_review(self):
        time_delta = datetime.timestamp(datetime.now()) - datetime.timestamp(
            self.publish_datetime
        )
        return (self.likes * self.watches) / log(time_delta)
