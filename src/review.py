from datetime import datetime


class Review:
    def __init__(
        self, title: str, likes: int, watches: int, publish_datetime: datetime
    ):
        self.title = title
        self.likes = likes
        self.watches = watches
        self.publish_datetime = publish_datetime

    def __repr__(self):
        return f"Title: {self.title}; rating: {self.calculate_rating_of_review()}"

    def calculate_rating_of_review(self):
        """
        Формула: likes/watches * 1/(curr_date - publish_date)
        """
        time_delta = datetime.timestamp(datetime.now()) - datetime.timestamp(
            self.publish_datetime
        )
        return ((self.likes / self.watches) * (1 / time_delta)) * 1000000
