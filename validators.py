from exceptions import MoveNotInRangeException


def validate_user_input(user_input):
    _user_input = int(user_input)
    if _user_input not in range(9):
        raise MoveNotInRangeException
    return _user_input
