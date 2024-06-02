def convert_number_with_K_notations_to_int(amount_of_watches: str) -> int:
    """
    Переводит запись вида nK в целое число n.

    Например:
    >>> convert_number_with_K_notations_to_int("2K")
    >>> 2000

    !K Латинская!
    """
    if "K" in amount_of_watches:
        k_index = amount_of_watches.find("K")
        number = int(amount_of_watches[:k_index])
        return number * 1000

    return int(amount_of_watches)
