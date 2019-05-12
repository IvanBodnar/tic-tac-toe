from board import LogicalBoard, PhysicalBoard
from game import Manager
from validators import validate_user_input
from exceptions import MoveNotInRangeException, FilledSquareException


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

        manager.register_move(move)
        win = manager.get_winner()
        if win:
            print(win.name + ' wins')
            break


if __name__ == '__main__':
    init()
