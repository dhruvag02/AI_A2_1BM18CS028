# Player and CPU Tic Tac Toe implementation
import random

theBoard = {7: ' ', 8: ' ', 9: ' ',
            4: ' ', 5: ' ', 6: ' ',
            1: ' ', 2: ' ', 3: ' '}

lst = list()
HUMAN = 'X'
COMPUTER = 'O'


def big(a, b):
    if a > b:
        return a
    else:
        return b


def hinderWin(count):
    if count == 4:
        if abs(lst[1] - lst[0]) == 1:#Row
            c = big(lst[0], lst[1])
            #theBoard[c + 1] = turn
            if c < 10:
                return c+1
            else:
                return c-1
        if abs(lst[1] - lst[0]) == 3:#Column
            c = big(lst[0], lst[1])
            #theBoard[c + 3] = turn
            if c < 10:
                return c+3
            else:
                return c-3
        if abs(lst[1] - lst[0]) == 4:#right diagonal
            c = big(lst[0], lst[1])
            #theBoard[c + 4] = turn
            if c < 10:
                return c+4
            else:
                return c-4
        if abs(lst[1] - lst[0]) == 2:#left diagonal
            c = big(lst[0], lst[1])
            #theBoard[c + 2] = turn
            if c < 10:
                return c+2
            else:
                return c-2


def checkWin(count, turn):
    # Check the win condition after 5 moves only
    if count >= 5:
        if theBoard[7] == theBoard[8] == theBoard[9] != ' ':  # across the top
            printBoard(theBoard)
            print("Game Over")
            print("*** " + turn + " won")
            return 1
        elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':  # across the middle
            printBoard(theBoard)
            print("Game Over")
            print("*** " + turn + " won")
            return 1
        elif theBoard[1] == theBoard[2] == theBoard[3] != ' ':  # across the bottom
            printBoard(theBoard)
            print("Game Over")
            print("*** " + turn + " won")
            return 1
        elif theBoard[1] == theBoard[4] == theBoard[7] != ' ':  # across the left column
            printBoard(theBoard)
            print("Game Over")
            print("*** " + turn + " won")
            return 1
        elif theBoard[2] == theBoard[5] == theBoard[8] != ' ':  # across the midlle column
            printBoard(theBoard)
            print("Game Over")
            print("*** " + turn + " won")
            return 1
        elif theBoard[3] == theBoard[6] == theBoard[9] != ' ':  # across the right column
            printBoard(theBoard)
            print("Game Over")
            print("*** " + turn + " won")
            return 1
        elif theBoard[7] == theBoard[5] == theBoard[3] != ' ':  # across the diagonal
            printBoard(theBoard)
            print("Game Over")
            print("*** " + turn + " won")
            return 1
        elif theBoard[1] == theBoard[5] == theBoard[9] != ' ':  # across the diagonal
            printBoard(theBoard)
            print("Game Over")
            print("*** " + turn + " won")
            return 1

    # if neither X nor O wins and board is full, result is declared as tie
    if count == 9:
        printBoard(theBoard)
        print("Game Over")
        print("It's a Tie")
        return 1


def printBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


#printBoard(theBoard)
def get_computer_move():
    return random.randint(1, 8)


def game():
    turn = 'X'
    if turn != 'X' and turn != 'O':
        print("Invalid Turn")
        quit()
    count = 0
    i = 0
    while True:
        printBoard(theBoard)
        if turn == 'X':
            if count == 4:
                move = hinderWin(count)
            else:
                move = get_computer_move()
            print("The value of move:", move)
        else:
            print("It's Your turn, " + turn + " Move to which place?")
            move = int(input())
            lst.append(move)
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count = count + 1
            # To know iterations
            print("Value of count ", count)
            print("Value of i ", i)
        else:
            print("This place is already filled.\n Move to which place?")
            i -= 1
            print(i)
            continue
        if count >= 5:
            c = checkWin(count, turn)
            if c == 1:
                quit()
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        i += 1


if __name__ == "__main__":
    game()


 | |
-+-+-
 | |
-+-+-
 | |
The value of move: 5
Value of count  1
Value of i  0
 | |
-+-+-
 |X|
-+-+-
 | |
It's Your turn, O Move to which place?
1
Value of count  2
Value of i  1
 | |
-+-+-
 |X|
-+-+-
O| |
The value of move: 6
Value of count  3
Value of i  2
 | |
-+-+-
 |X|X
-+-+-
O| |
It's Your turn, O Move to which place?
4
Value of count  4
Value of i  3
 | |
-+-+-
O|X|X
-+-+-
O| |
The value of move: 7
Value of count  5
Value of i  4
X| |
-+-+-
O|X|X
-+-+-
O| |
It's Your turn, O Move to which place?
8
Value of count  6
Value of i  5
X|O|
-+-+-
O|X|X
-+-+-
O| |
The value of move: 3
Value of count  7
Value of i  6
X|O|
-+-+-
O|X|X
-+-+-
O| |X
Game Over
*** X won
