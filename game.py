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
    def __init__(self, name, combination=None):
        self.name = name
        self.combination = combination


class Manager:
    def __init__(self, physical_board):
        self._board = physical_board
        self._human_moves = []
        self._computer_moves = []
        self._current_turn = None

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
            return Player('human', human_winning_combination)
        elif computer_winning_combination:
            return Player('computer', computer_winning_combination)
        else:
            return None

    def register_move(self, square: str, value: str):
        try:
            self._board.send_move(square, value)
            self._human_moves.append(square) if value == 'x' else self._computer_moves.append(square)
        except FilledSquareException:
            raise

    # def _set_random_turn(self):
    #     return (Player('human'), Player('computer'))

    def flip_turn(self):
        pass

