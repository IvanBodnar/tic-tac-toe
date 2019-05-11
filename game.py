from exceptions import FilledSquareException


class LogicalBoard:
    def __init__(self):
        self._board = {x: None for x in range(10)}
        self._occupied_squares = []

    def fill_square(self, square_number, value):
        if not self._board.get(square_number):
            self._board[square_number] = value
        else:
            raise FilledSquareException('Square is Occupied')
