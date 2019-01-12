#TicTacToe by James Oh

def drawBoard(board):
    print()
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def initializeBoard():
    return [' '] * 10

def selectLetter():
    letter = ""
    while letter != 'X' and letter != 'O':
        print("Do you want to be O or X?")
        letter = input()
    return letter

def switchPlayer(letter):
    if letter == 'O':
        return 'X'
    return 'O'

def makeMove(board, letter, move):
    board[move] = letter

def isValidMove(board, move):
    if move > 8 or move < 0 or board[move] != ' ':
        return False
    return True

def isBoardFull(board):
    for i in range(len(board)):
        if isValidMove(board, i):
            return False
    return True

def isWinner(board, letter):
    return ((board[0] == letter and board[1] == letter and board[2] == letter) or #Top row
            (board[3] == letter and board[4] == letter and board[5] == letter) or #Middle row
            (board[6] == letter and board[7] == letter and board[8] == letter) or #Bottom row
            (board[0] == letter and board[3] == letter and board[6] == letter) or #Left column
            (board[1] == letter and board[4] == letter and board[7] == letter) or #Middle column
            (board[2] == letter and board[5] == letter and board[8] == letter) or #Right column
            (board[0] == letter and board[4] == letter and board[8] == letter) or #One of the diagonal
            (board[2] == letter and board[4] == letter and board[6] == letter)) #Another diagonal

def playGame():
    board = initializeBoard()
    letter = selectLetter()
    while not isBoardFull(board):
        drawBoard(board)
        print("What is your move?")
        move = int(input())
        if isValidMove(board, move):
            makeMove(board, letter, move)
        else:
            print("invalid move")
            continue
        if isWinner(board, letter):
            print(letter + " have won!!!!")
            break
        letter = switchPlayer(letter)

def main() -> None:
    playGame()

if __name__ == '__main__':
    main()

