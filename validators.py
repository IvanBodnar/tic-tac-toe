from exceptions import MoveNotInRange


def validate_user_input(user_input):
    int(user_input)
    if user_input not in range(9):
        raise MoveNotInRange
