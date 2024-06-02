from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    title: str
    likes: int
    watches: int
    publish_datetime: datetime
    rating: float = 0.0

    def __str__(self):
        return f"Title: {self.title}; likes: {self.likes}; watches: {self.watches}; publish_date: {self.publish_datetime}, rating: {self.rating}"
