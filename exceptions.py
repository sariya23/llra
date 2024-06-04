class LandingException(Exception):
    pass


class WrongDatetimeFormatFromApp(LandingException):
    pass


class WrongMonthCaseFromApp(LandingException):
    pass
