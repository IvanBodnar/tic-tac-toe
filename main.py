from board import LogicalBoard, PhysicalBoard, WINNING_COMBINATIONS
from validators import validate_user_input
from exceptions import MoveNotInRangeException


b = LogicalBoard()
# b.fill_square(1, 'x')
p = PhysicalBoard(b)
p.draw()
p.register_move(1, 'x')


while True:
    try:
        move = validate_user_input(input('Enter move'))
    except ValueError:
        print('Must enter an integer')
        continue
    except MoveNotInRangeException:
        print('Must enter a value between 0 and 8')
        continue

