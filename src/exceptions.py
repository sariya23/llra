class LandingException(Exception):
    pass


class WrongDatetimeFormatFromApp(LandingException):
    pass


class WrongMonthCaseFromApp(LandingException):
    pass


class ArgsException(Exception):
    pass


class NoArguments(ArgsException):
    pass


class MissRequiredArgument(ArgsException):
    pass
