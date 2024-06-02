from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Article:
    title: str
    likes: int
    watches: int
    publish_datetime: datetime
