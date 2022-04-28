import random

board = [["","",""],["","",""],["","",""]]
playGame = True


def playerTurn():
    while True:
        while True:
            positionChoice = input("Where would you like to move?")
            if int(positionChoice) == 1:
                row = 0
                column = 0
            if int(positionChoice) == 2:
                row = 0
                column = 1
            if int(positionChoice) == 3:
                row = 0
                column = 2
            if int(positionChoice) == 4:
                row = 1
                column = 0
            if int(positionChoice) == 5:
                row = 1
                column = 1
            if int(positionChoice) == 6:
                row = 1
                column = 2
            if int(positionChoice) == 7:
                row = 2
                column = 0
            if int(positionChoice) == 8:
                row = 2
                column = 1
            if int(positionChoice) == 9:
                row = 2
                column = 2
            break
            else:
                continue
        if board[row][column] == "X" or board[row][column] == "O":
            continue
        else:
            board[row].pop(column)
            board[row].insert(column,"X")
            break

def computerTurn():
    while True:
        row = random.randint(0,2)
        column = random.randint(0,2)
        if board[row][column] == "X" or board[row][column] == "O":
            continue
        else:
            board[row].pop(column)
            board[row].insert(column,"O")
            break
def endGame():
    if board[0]== ["X","X","X"] or board[1]== ["X","X","X"] or board[2]== ["X","X","X"]:
        print("Player Wins!")
        exit()
    elif board[1]== ["X","X","X"] or board[1]== ["X","X","X"] or board[2]== ["X","X","X"]:
        print("Player Wins!")
        exit()
    elif board[2]== ["X","X","X"] or board[1]== ["X","X","X"] or board[2]== ["X","X","X"]:
        print("Player Wins!")
        exit()
    elif board[0][0] == "X" and board[1][0]=="X" and board[2][0]=="X":
        print("Player Wins!")
        exit()
    elif board[0][1] == "X" and board[1][1]=="X" and board[2][1]=="X":
        print("Player Wins!")
        exit()
    elif board[0][2] == "X" and board[1][2]=="X" and board[2][2]=="X":
        print("Player Wins!")
        exit()
    elif board[0][0] == "X" and board[1][1]=="X" and board[2][2]=="X":
        print("Player Wins!")
        exit()
    elif board[0][2] == "X" and board[1][1]=="X" and board[2][0]=="X":
        print("Player Wins!")
        exit()
    elif board[0]== ["O","O","O"] or board[1]== ["O","O","O"] or board[2]== ["O","O","O"]:
        print("Computer Wins!")
        exit()
    elif board[1]== ["O","O","O"] or board[1]== ["O","O","O"] or board[2]== ["O","O","O"]:
        print("Computer Wins!")
        exit()
    elif board[2]== ["O","O","O"] or board[1]== ["O","O","O"] or board[2]== ["O","O","O"]:
        print("Computer Wins!")
        exit()
    elif board[0][0] == "O" and board[1][0]=="O" and board[2][0]=="O":
        print("Computer Wins!")
        exit()
    elif board[0][1] == "O" and board[1][1]=="O" and board[2][1]=="O":
        print("Computer Wins!")
        exit()
    elif board[0][2] == "O" and board[1][2]=="O" and board[2][2]=="O":
        print("Computer Wins!")
        exit()
    elif board[0][0] == "O" and board[1][1]=="O" and board[2][2]=="O":
        print("Computer Wins!")
        exit()
    elif board[0][2] == "O" and board[1][1]=="O" and board[2][0]=="O":
        print("Computer Wins!")
        exit()

        
        
while playGame == True:
    playerTurn()
    print("____________")
    for row in board:
        print(row)
    print("____________")
    endGame()
    computerTurn()
    print("____________")
    for row in board:
        print(row)
    print("____________")
    endGame()
    
