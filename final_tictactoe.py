# Tic Tac Toe

import random

class Game:
    def __init__(self,board):
        self.board = board

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the first player's letter as the first item, and the second player's letter as the second.
        print('Does player 1 want to be X or O?')
        player1 = input().upper()
        while True:
            if player1 == 'X':
                player2 = 'O'
                print("Player 1 will be " + player1 + ". Player 2 will be " + player2)
                return player1.upper(), player2
            elif player1 == 'O':
                player2 = 'X'
                print("Player 1 will be " + player1 + ". Player 2 will be " + player2)
                return player1.upper(), player2
            else:
                player1 = input("Please pick X or O.").upper()

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'Player 1'
        else:
            return 'Player 2'

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isWinner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or # across the top
        (self.board[4] == le and self.board[5] == le and self.board[6] == le) or # across the middle
        (self.board[1] == le and self.board[2] == le and self.board[3] == le) or # across the bottom
        (self.board[7] == le and self.board[4] == le and self.board[1] == le) or # down the left side
        (self.board[8] == le and self.board[5] == le and self.board[2] == le) or # down the middle
        (self.board[9] == le and self.board[6] == le and self.board[3] == le) or # down the right side
        (self.board[7] == le and self.board[5] == le and self.board[3] == le) or # diagonal
        (self.board[9] == le and self.board[5] == le and self.board[1] == le)) # diagonal


    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def getPlayer1Move(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print('What is player 1\'s next move? (1-9)')
            move = input()
        return int(move)


    def getPlayer2Move(self):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print('What is player 2\'s next move? (1-9)')
            move = input()
        return int(move)


    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True


print('Welcome to Tic Tac Toe!')
print('The objective of the game is to get 3 in a row')
print('Decide who player 1 and player 2 is before playing')
print()
print('''These are the spaces and their corresponding numbers for reference
   |   |
 7 | 8 | 9
   |   |
-----------
   |   |
 4 | 5 | 6
   |   | 
-----------
   |   |
 1 | 2 | 3
   |   |
''')
while True:
    # Reset the board
    tic = Game([' '] * 10)
    player1Letter, player2Letter = tic.inputPlayerLetter()
    turn = tic.whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player 1':
            # Player1's turn.
            tic.drawBoard()
            move = tic.getPlayer1Move()
            tic.makeMove(player1Letter, move)

            if tic.isWinner(player1Letter):
                tic.drawBoard()
                print('Hooray! Player 1 has won the game!')
                gameIsPlaying = False
            else:
                if tic.isBoardFull():
                    tic.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            tic.drawBoard()
            move = tic.getPlayer2Move()
            tic.makeMove(player2Letter, move)

            if tic.isWinner(player2Letter):
                tic.drawBoard()
                print('Hooray! Player 2 has won the game!')
                gameIsPlaying = False
            else:
                if tic.isBoardFull():
                    tic.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not tic.playAgain():
        break
