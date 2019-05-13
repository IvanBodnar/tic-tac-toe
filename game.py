from random import choice

from exceptions import FilledSquareException


WINNING_COMBINATIONS = (
    {0, 1, 2},
    {3, 4, 5},
    {6, 7, 8},
    {0, 3, 4},
    {1, 4, 7},
    {2, 5, 8},
    {0, 4, 8},
    {6, 4, 2},
)


class Player:
    def __init__(self):
        self.name = None
        self.sign = None
        self.combination = None


class Human(Player):
    def __init__(self):
        super().__init__()
        self.sign = 'x'
        self.name = 'human'


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.sign = 'o'
        self.name = 'computer'


class Manager:
    def __init__(self, physical_board):
        self._board = physical_board
        self._human_moves = []
        self._computer_moves = []
        self._current_turn = self._set_random_turn()

    def init_board(self):
        self._board.draw()

    @staticmethod
    def is_winning_combination(combination: set) -> set:
        is_win = len([winning_comb for winning_comb in WINNING_COMBINATIONS if winning_comb <= combination]) > 0
        if is_win:
            return combination

    def get_winner(self):
        human_winning_combination = self.is_winning_combination(set(self._human_moves))
        computer_winning_combination = self.is_winning_combination(set(self._computer_moves))
        if human_winning_combination:
            return Human()
        elif computer_winning_combination:
            return Computer()
        else:
            return None

    def register_move(self, square: str):
        current_sign = self._current_turn.sign
        try:
            self._board.send_move(square, current_sign)
            self._human_moves.append(square) if current_sign == 'x' else self._computer_moves.append(square)
            self._flip_turn()
        except FilledSquareException:
            raise

    @staticmethod
    def _set_random_turn() -> Player:
        # return choice((Human(), Computer()))
        return Human()

    def _flip_turn(self):
        if isinstance(self._current_turn, Human):
            self._current_turn = Computer()
        elif isinstance(self._current_turn, Computer):
            self._current_turn = Human()

