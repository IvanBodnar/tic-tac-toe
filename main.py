from board import LogicalBoard, PhysicalBoard
from game import Manager
from validators import validate_user_input
from exceptions import MoveNotInRangeException, FilledSquareException
from computer_play import minimax, empty_squares


def init():
    logical_board = LogicalBoard()
    physical_board = PhysicalBoard(logical_board)
    manager = Manager(physical_board)

    manager.init_board()

    while True:
        try:
            move = validate_user_input(input('Enter move\n'))
        except ValueError:
            print('Must enter an integer')
            continue
        except MoveNotInRangeException:
            print('Must enter a value between 0 and 8')
            continue
        except FilledSquareException:
            print('That square is filled. Choose another one')
            continue


        depth = len(empty_squares(logical_board.state))
        if depth < 9:
            p = None
            if manager._current_turn.name == 'computer':
                p = 1
            else:
                p = -1
            x = minimax(logical_board.state.copy(), depth, p)
            print(x)

        manager.register_move(move)

        win = manager.get_winner()
        if win:
            print(win.name + ' wins')
            break


if __name__ == '__main__':
    init()
