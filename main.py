# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def assignment2():
    # get users name
    name = input("Tell me your name:")
    print(f'Hello {name}')
    # enter a number and multiply by itself
    x = int(input("Enter a number: "))
    print(x * x)
    #enter a word and calculate letter number
    word = input("Please enter a word: ")
    print("The number of letters in the word is: ", len(word))
import random
def assignment3():
    #Print 2-d array
    rows = 9
    col = 9
    grid = [[0, 0, 0, 0, 0]]
    for i in range(rows):
        print("".join('.' for j in range(col)))
    #Coin Flip
    coin = int(input("Enter a value 1 or 0: "))
    flip = random.randint(0, 1)
    if(coin == flip):
        print("You win!")
    else:
        print("You lose!")

from random import randrange
def display_board(board):
    #print board w/ display in center of 7x7
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    valid = False
    #input move, determine if valid, if not, rerun
    while not valid:
        move = input("Enter move: ")
        valid = len(move) == 1 and move >= '1' and move <= '9'
        if not valid:
            print("ERROR: Repeat input!")
            continue
        # cell numb from 0-8
        move = int(move) - 1
        row = move // 3  # cell's row
        col = move % 3  # cell's column
        # check the selected square
        sign = board[row][col]
        valid = sign not in ['O', 'X']
        if not valid:
            print("Spot taken: repeat input!")
            continue
    board[row][col] = 'O'  # place move '0' at the location

def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            # is the cell free?
            if board[row][col] not in ['O', 'X']:
                free.append((row, col))
    return free


def victory_for(board, sign):
    #who won, figure it out
    if sign == "X":
        who = 'me'
    elif sign == "O":
        who = 'you'
    else:
        who = None
    cross1 = cross2 = True  # for diagonals
    for rc in range(3):
        # check row rc
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            return who
        # check column rc
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            return who
        # check 1st diag
        if board[rc][rc] != sign:
            cross1 = False
        # check 2nd diag
        if board[2 - rc][2 - rc] != sign:
            cross2 = False
    if cross1 or cross2:
        return who
    return None

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    #assignment2()
    #assignment3()

def draw_move(board):
    # make a list of free fields
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'

# make an empty board
board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
board[1][1] = 'X'
free = make_list_of_free_fields(board)
humturn = True

while len(free):
	display_board(board)
	if humturn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	humturn = not humturn
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/