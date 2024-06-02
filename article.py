from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class Article:
    title: str
    likes: int
    watches: int
    publish_date: date
