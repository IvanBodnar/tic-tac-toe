from exceptions import FilledSquareException


class LogicalBoard:
    def __init__(self):
        self._board = {x: None for x in range(9)}
        self._filled_squares = set()

    def fill_square(self, square_number: str, value: str):
        if square_number in self._filled_squares:
            raise FilledSquareException()
        self._board[square_number] = value
        self._filled_squares.add(square_number)

    def get_filled_squares(self):
        return self._filled_squares

    @property
    def state(self):
        return self._board

    def __str__(self):
        return str(self._board)


class PhysicalBoard:
    def __init__(self, logical_board: LogicalBoard):
        self.logical_board = logical_board

    def draw(self):
        board_state = self.logical_board.state
        print('|', board_state.get(0) or 0, '|', board_state.get(1) or 1, '|', board_state.get(2) or 2, '|')
        print('|', board_state.get(3) or 3, '|', board_state.get(4) or 4, '|', board_state.get(5) or 5, '|')
        print('|', board_state.get(6) or 6, '|', board_state.get(7) or 7, '|', board_state.get(8) or 8, '|')

    def send_move(self, square: str, value: str):
        self.logical_board.fill_square(square, value)
        self.draw()
