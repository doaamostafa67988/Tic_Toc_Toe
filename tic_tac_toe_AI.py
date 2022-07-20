board=['-','-','-','-','-','-','-','-','-']
def dis():
  print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
  print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
  print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")

def spaceIsFree(position):
    if board[position] == '-':
      return True
    else:
      return False
def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        dis()
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        return


    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return
def checkForWin():
    if (board[0] == board[1]  == board[2] and board[0] != '-'):
        return True
    elif (board[3] == board[4]  == board[5] and board[3] != '-'):
        return True

    elif (board[6] == board[7] == board[8] and board[6] != '-'):
        return True
    elif (board[0] == board[3] == board[6] and board[0] != '-'):
        return True

    elif (board[1] == board[4]  == board[7] and board[1] != '-'):
        return True
    elif (board[2] == board[5]  == board[8] and board[2] != '-'):
        return True
    elif (board[0] == board[4] == board[8] and board[0] != '-'):
        return True
    elif (board[6] == board[4] == board[2] and board[6] != '-'):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if board[0] == board[1] == board[2] and board[0] == mark:
        return True
    elif (board[3] == board[4]  == board[5] and board[3] == mark):
        return True
    elif (board[6] == board[7] == board[8] and board[6] == mark):
        return True
    elif (board[0] == board[3]  == board[6] and board[0] == mark):
        return True
    elif (board[1] == board[4] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5]  == board[8] and board[2] == mark):
        return True
    elif (board[0] == board[4]  == board[8] and board[0] == mark):
        return True
    elif (board[6] == board[4]  == board[2] and board[6] == mark):
        return True
    else:
        return False

def checkDraw():
    for i in range(9):
        if (board[i] == '-'):
            return False
    return True
def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return


def compMove():
    bestScore = -800
    bestMove = 0
    for i in range(9):
        if (board[i] == '-'):
            board[i] = bot
            score = minimax(board, 0, False)
            board[i] = '-'
            if (score > bestScore):
                bestScore = score
                bestMove = i

    insertLetter(bot, bestMove)
    return
def minimax(board, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for i in range(9):
            if (board[i] == '-'):
                board[i] = bot
                score = minimax(board, depth + 1, False)
                board[i] = '-'
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for i in range(9):
            if (board[i] == '-'):
                board[i] = player
                score = minimax(board, depth + 1, True)
                board[i] = '-'
                if (score < bestScore):
                    bestScore = score
        return bestScore

dis()
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("0, 1, 2 ")
print("3, 4, 5 ")
print("6, 7, 8 ")
print("\n")
player = 'O'
bot = 'X'
global firstComputerMove
firstComputerMove = True


while not checkForWin():
    compMove()
    playerMove()
