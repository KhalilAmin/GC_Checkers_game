import numpy
from numpy import random

def build_board(board_size):
    board = random.choice(['Empty', 'Red', 'Black'], (board_size, board_size))
    return board

def get_count(board, value):
    count = 0
    for a_list in board:
        for a_value in a_list:
            if a_value == value:
                count += 1
    return {value: count}

if __name__ == "__main__":
    print("This file can't be run as a main file")