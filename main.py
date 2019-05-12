from board import LogicalBoard, PhysicalBoard, WINNING_COMBINATIONS
from validators import validate_user_input
from exceptions import MoveNotInRangeException


b = LogicalBoard()
p = PhysicalBoard(b)
p.draw()


while True:
    try:
        move = validate_user_input(input('Enter move\n'))
    except ValueError:
        print('Must enter an integer')
        continue
    except MoveNotInRangeException:
        print('Must enter a value between 0 and 8')
        continue

    p.register_move(move, 'x')

