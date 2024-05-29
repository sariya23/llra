from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Article:
    title: str
    likes: int
    watches: int