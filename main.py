# Tic Tac Toe game in python

board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


#* This function checks if the board position is equal to an empty space
#* If it is, it returns True, else it returns False
#* The function is later called in the playerMove() function
def spaceIsFree(pos):
    return board[pos] == ' '


#* This function is used to create the layout of the board in a 3x3 grid
def printBoard(board):
    print('  |  |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('  |  |')
    print('-----------')
    print('  |  |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('  |  |')
    print('-----------')
    print('  |  |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('  |  |')

#* Function checks if any of the grids contain the same letter 'X' or 'O'
#* If there is match, then True is returned, else False
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[1] == le and bo[4] == le and bo[7] == le) or 
    (bo[2] == le and bo[5] == le and bo[8] == le) or 
    (bo[3] == le and bo[6] == le and bo[9] == le) or 
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le)


#* This function is used to get the player's move while 'run' = true
#* once run = false, the function terminates
#* run is set to false once the the player enters a valid command and their move is inserted on the board
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move) #Checks to see if input is an integer
            if move > 0 and move < 10: #Needs to be a valid position on the board
                if spaceIsFree(move): #checks if the space is available
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def compMove():
    pass

def selectRandom(board):
    pass

def isboardFull(board):
    if board.count(' ') > 1:
        return True
    else:
        return False



def main():
    print('Welcome to Tic Tac Toe! Good luck!')

    while not (isboardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print('Sorry buddy, you have been beaten by O\'s')
    

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', board)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard()
        
        else:
            print('X\'s have won! Congratulations!')


    if isboardFull(board):
        print('Tie Game! Better luck next time!')


main()