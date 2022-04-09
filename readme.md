Simple Tic Tac Toe program


# How It Works

1. Program starts and a blank 3x3 grid is printed 
2. The program checks to see if there any free spaces, if so the game continues
3. The user is asked to enter a number 1-9
4. After the input is received it is checked:
   1. If the input is an integer
   2. If that integer is between 1-9
   3. If the integer corresponds to a 'free' or unnoccupied spot on the board
      1. If yes, the spot is marked with an 'X'
      2. If no, the player is asked to input a different number
5. The board is checked again to see if the players move resulted in a win
   1. If yes, the game is finished
   2. If not, the computer gets a turn if there are available spaces left
6. The computer chooses their move using the logic:
   1. Creates a list of possible moves
   2. Checks to see if any of those moves will result in the player or computer winning 
      1. If the computer has a winning move, it will take it
      2. If the the player's next move will result in a win, the computer will block it
      3. If neither are true, computer checks for open spots in this order:
         1. Corners
         2. Center
         3. Edges
      4. Computer uses the random() function to pick out of the possible move choices
7. Program checks to see if there are any open spaces left. If so, the game continues
