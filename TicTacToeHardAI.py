import random
board = [["","",""],["","",""],["","",""]]

playGame = True
    
def playerTurn():
    while True:
        while True:
            positionChoice = input("Where would you like to move?")
            if positionChoice == "1":
                row = 0
                column = 0
                break
            if positionChoice == "2":
                row = 0
                column = 1
                break
            if positionChoice == "3":
                row = 0
                column = 2
                break
            if positionChoice == "4":
                row = 1
                column = 0
                break
            if positionChoice == "5":
                row = 1
                column = 1
                break
            if positionChoice == "6":
                row = 1
                column = 2
                break
            if positionChoice == "7":
                row = 2
                column = 0
                break
            if positionChoice == "8":
                row = 2
                column = 1
                break
            if positionChoice == "9":
                row = 2
                column = 2
                break
            else:
                continue
        if board[int(row)][int(column)] == "X" or board[int(row)][int(column)] == "O":
            print("That spot's already taken.")
            continue
        else:
            board[int(row)].pop(int(column))
            board[int(row)].insert(int(column),"X")
            break
def pickRandom():
    while True:
        choice = random.randint(1,9)
        if choice == 1:
            row = 0
            column = 0
        if choice == 2:
            row = 0
            column = 1
        if choice == 3:
            row = 0
            column = 2
        if choice == 4:
            row = 1
            column = 0
        if choice == 5:
            row = 1
            column = 1
        if choice == 6:
            row = 1
            column = 2
        if choice == 7:
            row = 2
            column = 0
        if choice == 8:
            row = 2
            column = 1
        if choice == 9:
            row = 2
            column = 2
        if board[row][column] == "X" or board[row][column] == "O":
            continue
        else:
            board[row].pop(column)
            board[row].insert(column,"O")
            break
        
def computerTurn():
    required = False
#_______________________________________________________________________________________________________________________
    #Special rules
    if board == [["X","","X"],["","O",""],["X","","O"]]:
        board[0].pop(1)
        board[0].insert(1,"O")
        required = True
    if board == [["O","","X"],["","O",""],["X","","X"]]:
        board[1].pop(2)
        board[1].insert(2,"O")
        required = True
    if board == [["X","","O"],["","O",""],["X","","X"]]:
        board[1].pop(0)
        board[1].insert(0,"O")
        required = True
    if board == [["X","","X"],["","O",""],["O","","X"]]:
        board[0].pop(1)
        board[0].insert(1,"O")
        required = True
#____________________________________________________________________________________________________
    #If player starts center
    if board == [["","",""],["","X",""],["","",""]]:
        board[0].pop(0)
        board[0].insert(0,"O")
        required = True
    elif board== [["X","",""],["","",""],["","",""]] or board== [["","X",""],["","",""],["","",""]] or board== [["","","X"],["","",""],["","",""]] or board== [["","",""],["X","",""],["","",""]] or board== [["","",""],["","","X"],["","",""]] or board== [["","",""],["","",""],["X","",""]] or board== [["","",""],["","",""],["","X",""]] or board== [["","",""],["","",""],["","","X"]]: 
        board[1].pop(1)
        board[1].insert(1,"O")
        required = True

#_______________________________________________________________________________________________________
    #Win top across
    if board[0][0] == "O" and board[0][1]=="O" and board[0][2]=="":
        board[0].pop(2)
        board[0].insert(2,"O")
    elif board[0][0] == "" and board[0][1]=="O" and board[0][2]=="O":
        board[0].pop(0)
        board[0].insert(0,"O")
    elif board[0][0] == "O" and board[0][1]=="" and board[0][2]=="O":
        board[0].pop(1)
        board[0].insert(1,"O")
    #Win middle across
    elif board[1][0] == "O" and board[1][1]=="O" and board[1][2]=="":
        board[1].pop(2)
        board[1].insert(2,"O")
    elif board[1][0] == "" and board[1][1]=="O" and board[1][2]=="O":
        board[1].pop(0)
        board[1].insert(0,"O")
    elif board[2][0] == "O" and board[2][1]=="" and board[2][2]=="O":
        board[2].pop(1)
        board[2].insert(1,"O")
    #Win bottom across
    elif board[2][0] == "O" and board[2][1]=="O" and board[2][2]=="":
        board[2].pop(2)
        board[2].insert(2,"O")
    elif board[2][0] == "" and board[2][1]=="O" and board[2][2]=="O":
        board[2].pop(0)
        board[2].insert(0,"O")
    elif board[2][0] == "O" and board[2][1]=="" and board[2][2]=="O":
        board[2].pop(1)
        board[2].insert(1,"O")
    #Win left column
    elif board[0][0] == "O" and board[1][0]=="O" and board[2][0]=="":
        board[2].pop(0)
        board[2].insert(0,"O")
    elif board[0][0] == "" and board[1][0]=="O" and board[2][0]=="O":
        board[0].pop(0)
        board[0].insert(0,"O")
    elif board[0][0] == "O" and board[1][0]=="" and board[2][0]=="O":
        board[1].pop(0)
        board[1].insert(0,"O")
    #Win center column
    elif board[0][1] == "O" and board[1][1]=="O" and board[2][1]=="":
        board[2].pop(1)
        board[2].insert(1,"O")
    elif board[0][1] == "" and board[1][1]=="O" and board[2][1]=="O":
        board[0].pop(1)
        board[0].insert(1,"O")
    elif board[0][1] == "O" and board[1][1]=="" and board[2][1]=="O":
        board[1].pop(1)
        board[1].insert(1,"O")
    #Win  right column
    elif board[0][2] == "O" and board[1][2]=="O" and board[2][2]=="":
        board[2].pop(2)
        board[2].insert(2,"O")
    elif board[0][2] == "" and board[1][2]=="O" and board[2][2]=="O":
        board[0].pop(2)
        board[0].insert(2,"O")
    elif board[0][2] == "O" and board[1][2]=="" and board[2][2]=="O":
        board[1].pop(2)
        board[1].insert(2,"O")
    #Win  diagonal top right to bottom left
    elif board[0][0] == "X" and board[1][1]=="X" and board[2][2]=="":
        board[2].pop(2)
        board[2].insert(2,"O")
    elif board[0][0] == "" and board[1][1]=="X" and board[2][2]=="X":
        board[0].pop(0)
        board[0].insert(0,"O")
    #Win diagonal top left to bottom right
    elif board[0][2] == "X" and board[1][1]=="X" and board[2][0]=="":
        board[2].pop(0)
        board[2].insert(0,"O")
    elif board[0][2] == "X" and board[1][1]=="X" and board[2][0]=="":
        board[2].pop(0)
        board[2].insert(0,"O")
#_______________________________________________________________________________________________________
    #Block player top across
    elif board[0][0] == "X" and board[0][1]=="X" and board[0][2]=="":
        board[0].pop(2)
        board[0].insert(2,"O")
    elif board[0][0] == "" and board[0][1]=="X" and board[0][2]=="X":
        board[0].pop(0)
        board[0].insert(0,"O")
    elif board[0][0] == "X" and board[0][1]=="" and board[0][2]=="X":
        board[0].pop(1)
        board[0].insert(1,"O")
    #Block player middle across
    elif board[1][0] == "X" and board[1][1]=="X" and board[1][2]=="":
        board[1].pop(2)
        board[1].insert(2,"O")
    elif board[1][0] == "" and board[1][1]=="X" and board[1][2]=="X":
        board[1].pop(0)
        board[1].insert(0,"O")
    elif board[2][0] == "X" and board[2][1]=="" and board[2][2]=="X":
        board[2].pop(1)
        board[2].insert(1,"O")
    #Block player bottom across
    elif board[2][0] == "X" and board[2][1]=="X" and board[2][2]=="":
        board[2].pop(2)
        board[2].insert(2,"O")
    elif board[2][0] == "" and board[2][1]=="X" and board[2][2]=="X":
        board[2].pop(0)
        board[2].insert(0,"O")
    elif board[2][0] == "X" and board[2][1]=="" and board[2][2]=="X":
        board[2].pop(1)
        board[2].insert(1,"O")
    #Block player left column
    elif board[0][0] == "X" and board[1][0]=="X" and board[2][0]=="":
        board[2].pop(0)
        board[2].insert(0,"O")
    elif board[0][0] == "" and board[1][0]=="X" and board[2][0]=="X":
        board[0].pop(0)
        board[0].insert(0,"O")
    elif board[0][0] == "X" and board[1][0]=="" and board[2][0]=="X":
        board[1].pop(0)
        board[1].insert(0,"O")
    #Block player center column
    elif board[0][1] == "X" and board[1][1]=="X" and board[2][1]=="":
        board[2].pop(1)
        board[2].insert(1,"O")
    elif board[0][1] == "" and board[1][1]=="X" and board[2][1]=="X":
        board[0].pop(1)
        board[0].insert(1,"O")
    elif board[0][1] == "X" and board[1][1]=="" and board[2][1]=="X":
        board[1].pop(1)
        board[1].insert(1,"O")
    #Block player right column
    elif board[0][2] == "X" and board[1][2]=="X" and board[2][2]=="":
        board[2].pop(2)
        board[2].insert(2,"O")
    elif board[0][2] == "" and board[1][2]=="X" and board[2][2]=="X":
        board[0].pop(2)
        board[0].insert(2,"O")
    elif board[0][2] == "X" and board[1][2]=="" and board[2][2]=="X":
        board[1].pop(2)
        board[1].insert(2,"O")
    #Block player diagonal top right to bottom left
    elif board[0][0] == "X" and board[1][1]=="X" and board[2][2]=="":
        board[2].pop(2)
        board[2].insert(2,"O")
    elif board[0][0] == "" and board[1][1]=="X" and board[2][2]=="X":
        board[0].pop(0)
        board[0].insert(0,"O")
    #Block player diagonal top left to bottom right
    elif board[0][2] == "X" and board[1][1]=="X" and board[2][0]=="":
        board[2].pop(0)
        board[2].insert(0,"O")
    elif board[0][2] == "X" and board[1][1]=="X" and board[2][0]=="":
        board[2].pop(0)
        board[2].insert(0,"O")
    elif required == False:
        pickRandom()
        
   
    
    

    
        
    
def endGame():
    if board[0]== ["X","X","X"] or board[1]== ["X","X","X"] or board[2]== ["X","X","X"]:
        print("Player Wins!")
        quit()
    elif board[1]== ["X","X","X"] or board[1]== ["X","X","X"] or board[2]== ["X","X","X"]:
        print("Player Wins!")
        quit()
    elif board[2]== ["X","X","X"] or board[1]== ["X","X","X"] or board[2]== ["X","X","X"]:
        print("Player Wins!")
        quit()
    elif board[0][0] == "X" and board[1][0]=="X" and board[2][0]=="X":
        print("Player Wins!")
        quit()
    elif board[0][1] == "X" and board[1][1]=="X" and board[2][1]=="X":
        print("Player Wins!")
        quit()
    elif board[0][2] == "X" and board[1][2]=="X" and board[2][2]=="X":
        print("Player Wins!")
        quit()
    elif board[0][0] == "X" and board[1][1]=="X" and board[2][2]=="X":
        print("Player Wins!")
        quit()
    elif board[0][2] == "X" and board[1][1]=="X" and board[2][0]=="X":
        print("Player Wins!")
        quit()
    elif board[0]== ["O","O","O"] or board[1]== ["O","O","O"] or board[2]== ["O","O","O"]:
        print("Computer Wins!")
        quit()
    elif board[1]== ["O","O","O"] or board[1]== ["O","O","O"] or board[2]== ["O","O","O"]:
        print("Computer Wins!")
        quit()
    elif board[2]== ["O","O","O"] or board[1]== ["O","O","O"] or board[2]== ["O","O","O"]:
        print("Computer Wins!")
        quit()
    elif board[0][0] == "O" and board[1][0]=="O" and board[2][0]=="O":
        print("Computer Wins!")
        quit()
    elif board[0][1] == "O" and board[1][1]=="O" and board[2][1]=="O":
        print("Computer Wins!")
        quit()
    elif board[0][2] == "O" and board[1][2]=="O" and board[2][2]=="O":
        print("Computer Wins!")
        quit()
    elif board[0][0] == "O" and board[1][1]=="O" and board[2][2]=="O":
        print("Computer Wins!")
        quit()
    elif board[0][2] == "O" and board[1][1]=="O" and board[2][0]=="O":
        print("Computer Wins!")
        quit()
    elif (board[0][0] == "O" or board[0][0] == "X")and (board[0][1] == "O" or board[0][1] == "X")and (board[0][2] == "O" or board[0][2] == "X") and (board[1][0] == "O" or board[1][0] == "X") and (board[1][1] == "O" or board[1][1] == "X") and (board[1][2] == "O" or board[1][2] == "X") and (board[2][0] == "O" or board[2][0] == "X") and (board[2][1] == "O" or board[2][1] == "X") and (board[2][2] == "O" or board[2][2] == "X"):
        print("It's a tie!")
        quit()
        
        
        
        
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
                    
