from src.review import Review


class OutputReview:
    def __init__(self, reviews: list[Review]) -> None:
        self.__reviews = reviews

    def output_in_file(self, file_name: str = "res.txx") -> None:
        with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
            for i, r in enumerate(self.__reviews, 1):
                f.write(f"{i}. {r}\n")

    def output_in_stdout(self) -> None:
        for i, r in enumerate(self.__reviews, 1):
            print(f"{i}. {r}")
