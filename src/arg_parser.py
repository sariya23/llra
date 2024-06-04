from src.exceptions import MissRequiredArgument, NoArguments


class ArgParser:
    """
    Класс парсит аргументы, переданные при запуске программы.
    Формат аргумента --arg_name=arg_value.
    """

    def __init__(self, args: list[str]) -> None:
        if len(args) < 1:
            raise NoArguments("No arguments. Miss required argument 'username'")
        self.args = args

    def __map_arg_name_and_value(self):
        arg_name_value = {}
        for arg in self.args:
            if "username" in arg:
                arg_name_value["username"] = self.get_value_from_arg(arg)
            elif "reverse" in arg:
                arg_name_value["reverse"] = self.get_value_from_arg(arg)
            elif "in_file" in arg:
                arg_name_value["in_file"] = self.get_value_from_arg(arg)

        return arg_name_value

    def set_value_of_args_true_false_default(self) -> dict[str, bool]:
        args = self.__map_arg_name_and_value()
        username = args.get("username")
        if username is None or username == "":
            raise MissRequiredArgument("Miss required argument 'username'")

        args["reverse"] = self.__parse_reverse(args.get("reverse"))
        args["in_file"] = self.__parse_in_file(args.get("in_file"))

        return args

    @staticmethod
    def __parse_reverse(reverse: str) -> bool:
        if reverse not in ("true", "false"):
            return True
        elif reverse == "true":
            return True
        else:
            return False

    @staticmethod
    def __parse_in_file(in_file: str) -> bool:
        if in_file not in ("true", "false"):
            return False
        elif in_file == "true":
            return True
        else:
            return False

    @staticmethod
    def get_value_from_arg(arg) -> str:
        return arg.split("=")[1]
