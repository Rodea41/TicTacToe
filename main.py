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
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#* Function checks if any of the grids contain the same letter 'X' or 'O'
#* If there is match, then True is returned, else False

def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)


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


#* This function will determine the logic the computer takes when selecting its move
#* It will start by checking if it can make a move to win the game, if not then it will check if
#* if there is a move to block the player from winning the game

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0 ] # Creates a list of all possible moves on the board for the AI
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:] # Creates a copy of the board
            boardCopy[i] = let 
            if isWinner(boardCopy, let): # Checks to see if the move will result in a win, if so, that will be the move the computer takes
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0: # Only runs if the cornersOpen list is not empty, i.e there are more than 0 corners open
        move = selectRandom(cornersOpen) # computer will select a random corner to move to 
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = [] # This is the same code as checking for corners, but it will check for edges. 
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:  
        move = selectRandom(edgesOpen)
    
    return move


#* This is the function that we put our 'cornersOpen' or 'edgesOpen' into to select a random number from it.
#* This function is used in the compMove() function above. 

def selectRandom(li):
    import random 
    ln = len(li) # Get the length of the list
    r = random.randrange(0, ln) 
    return li[r]



#* Checks to see if there are any open spaces left on the board. If yes, then the game continues, else the game ends
def isboardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


#! Main function
def main():
    print('Welcome to Tic Tac Toe! Good luck!')
    printBoard(board)

    while not (isboardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry buddy, you have been beaten by O\'s')
    

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        
        else:
            print('X\'s have won! Congratulations!')


    if isboardFull(board):
        print('Tie Game! Better luck next time!')


main()