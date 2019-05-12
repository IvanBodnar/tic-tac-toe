from board import PhysicalBoard
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


class Manager:
    def __init__(self, physical_board: PhysicalBoard):
        self._board = physical_board
        self._human_moves = []
        self._computer_moves = []

    def init_board(self):
        self._board.draw()

    def register_move(self, square: str, value: str):
        try:
            self._board.send_move(square, value)
            self._human_moves.append(square) if value == 'x' else self._computer_moves.append(square)
        except FilledSquareException:
            raise
