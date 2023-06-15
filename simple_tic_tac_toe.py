#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randrange


def display_board(board: list) -> None:
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print_row_divisor()
    for row in board:
        print_board_row(row)


def print_board_row(row: list):
    print_middle_row()
    print("|", end="")
    for val in row:
        print_row_with_value(val)
    print()
    print_middle_row()
    print_row_divisor()
        
    
def print_row_divisor() -> None:
    print("+" + ("-" * 7 + "+") * 3)


def print_middle_row() -> None:
    print("|" + (" " * 7 + "|") * 3)


def print_row_with_value(value: str) -> None:
    print(f"   {value}   |", end="")


def enter_move(board: list) -> list:
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    user_input = input("Enter your move: ")
    if user_input.isnumeric():
        move = int(user_input)
        if 0 < move < 10:
            x = (move - 1) // 3
            y = move % 3 - 1
            if board[x][y] == move:
                board[x][y] = "O"
            else:
                print("Field already occupied. You can't play here.")
                board = enter_move(board)
        else:
            print("The number must be between 1 and 9.")
            board = enter_move(board)
    else:
        print("You must type a number between 1 and 9.")
    display_board(board)
    if victory_for(board, 'O'):
        print("You won!")
        exit(0)
    return board


def make_list_of_free_fields(board: list) -> list:
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_moves = []
    for x in range(3):
        for y in range(3):
            if board[x][y] != 'X' and board[x][y] != 'O':
                free_moves.append((x,y))
    if free_moves:
        return free_moves
    else:
        print("Draw!")
        exit(0)


def victory_for(board: list, sign: str) -> bool:
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    diag_1 = []
    diag_2 = []
    for x in range(3):
        column = []
        row = []
        for y in range(3):
            row.append(board[x][y])
            column.append(board[y][x])
        if row.count(sign) == len(row) or column.count(sign) == len(column):
            return True
        diag_1.append(board[x][x])
        diag_2.append(board[x][2-x])
    if diag_1.count(sign) == len(diag_1) or diag_2.count(sign) == len(diag_2):
        return True
    else:
        return False


def draw_move(board: list) -> list:
    # The function draws the computer's move and updates the board.
    free_moves = make_list_of_free_fields(board)
    number_of_free_moves = len(free_moves)
    move = free_moves[randrange(number_of_free_moves)]
    board[move[0]][move[1]] = "X"
    display_board(board)
    if victory_for(board, 'X'):
        print("Game over!")
        exit(0)
    if number_of_free_moves == 1:
        print("Draw!")
        exit(0)
    return board


def init_board() -> list:
    board = []
    for x in range(3):
        board.append([])
        for y in range(3):
            board[x].append(y+(x*3)+1)
    board[1][1] = "X"
    return board


def main() -> int:
    board = init_board()
    display_board(board)
    while True:
        board = enter_move(board)
        board = draw_move(board)
	return 0

if __name__ == "__main__":
    main()
