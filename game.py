from exceptions import FilledSquareException


WINNING_COMBINATIONS = (
    (0, 1, 2,),
    (3, 4, 5,),
    (6, 7, 8,),
    (0, 3, 4,),
    (1, 4, 7,),
    (2, 5, 8,),
    (0, 4, 8,),
    (6, 4, 2,),
)


class LogicalBoard:
    def __init__(self):
        self._board = {x: None for x in range(9)}
        self._filled_squares = set()

    def fill_square(self, square_number, value):
        if square_number in self._filled_squares:
            raise FilledSquareException('Square is Filled')
        self._board[square_number] = value
        self._filled_squares.add(square_number)

    def get_filled_squares(self):
        return self._filled_squares

    @property
    def state(self):
        return self._board

    def check_is_winning_combination(self, combination):
        if combination in WINNING_COMBINATIONS:
            return {self._board.get(key) for key in combination}

    def __str__(self):
        return str(self._board)
