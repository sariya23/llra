import sys

from src.arg_parser import ArgParser
from src.utils import get_all_reviews_of_user

if __name__ == "__main__":
    arg_parser = ArgParser(sys.argv[1:])
    args = arg_parser.set_value_of_args_true_false_default()

    reviews = get_all_reviews_of_user(args["username"])

    if not args["in_file"]:
        for review in sorted(
            reviews,
            key=lambda r: r.calculate_rating_of_review(),
            reverse=args["reverse"],
        ):
            print(review)
