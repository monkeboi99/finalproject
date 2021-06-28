# Tic Tac Toe

import random

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
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

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayer1Move(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is player 1\'s next move? (1-9)')
        move = input()
    return int(move)


def getPlayer2Move(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is player 2\'s next move? (1-9)')
        move = input()
    return int(move)


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1Letter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player 1':
            # Player1's turn.
            drawBoard(theBoard)
            move = getPlayer1Move(theBoard)
            makeMove(theBoard, player1Letter, move)

            if isWinner(theBoard, player1Letter):
                drawBoard(theBoard)
                print('Hooray! Player 1 has won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            drawBoard(theBoard)
            move = getPlayer2Move(theBoard)
            makeMove(theBoard, player2Letter, move)

            if isWinner(theBoard, player2Letter):
                drawBoard(theBoard)
                print('Yay! Player 2 has won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not playAgain():
        break
