import argparse

from src.utils import get_all_reviews_of_user

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--username", type=str, help="Required user name", required=True
    )
    arg_parser.add_argument(
        "--in_file", action="store_true", help="Write result in file"
    )
    arg_parser.add_argument(
        "--asc_sort",
        action="store_false",
        help="The order of sort is ascending. Deafult is descending sort",
    )
    args = arg_parser.parse_args()
    reviews = get_all_reviews_of_user()
    reviews = sorted(
        reviews,
        key=lambda r: r.calculate_rating_of_review(),
        reverse=args["reverse"],
    )

    if args["in_file"]:
        with open("res.txt", "w", encoding="utf-8") as f:
            f.writelines([f"{str(r)}\n" for r in reviews])
    else:
        print(*reviews, sep="\n")
