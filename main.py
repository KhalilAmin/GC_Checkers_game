import checkers
from numpy import unique
def game():
    bSize = int(input("Enter the size of the board: "))
    mBoard = checkers.build_board(bSize)
    print(mBoard)
    list_values = unique(mBoard)
    count = {}
    for values in list_values:
        count.update(checkers.get_count(mBoard, values))
    print(f'\n {count}')


if __name__ == "__main__":
    game()