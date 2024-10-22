from random import randrange

def display_board(board):
    for i in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for j in i:
            print("|",j,sep="   ",end="   ")
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def victory_for(board, sign):
    # pe linie
    for i in board:
        verif=1
        for j in i:
            if j!=sign:
                verif=0
        if verif==1:
            return True
    
    #pe coloana
    for j in range(len(board[0])):
        verif=1
        for i in range(len(board)):
            if board[i][j]!=sign:
                verif=0
        if verif==1:
            return True
    
    #pe diagonala
    if board[1][1]==sign:
        if (board[0][0]==sign and board[2][2]==sign) or (board[0][2]==sign and board[2][0]==sign):
            return True
  
    return False

def enter_move(board):
    #mutarea jucatorului
    while True:
        move=int(input("Enter your move: "))
        if move>0 and move<10 and any(move in i for i in board):
            break
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==move:
                board[i][j]='O'
                break

    #mutarea calculatorului
    while True:
        move=randrange(10)
        if any(move in i for i in board):
            break
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==move:
                board[i][j]='X'
                break
    
def make_list_of_free_fields(board):
    tuple=()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!='O' and board[i][j]!='X':
                tuple+=((i,j),)
    return tuple

def state_of_game(board):
    if victory_for(board,'X'):
        return 1
    if victory_for(board,'O'):
        return 2
    return 0
    
board=[[1,2,3],[4,"X",6],[7,8,9]]
state=0 # 0-in game/draw 1-lose 2-win
while state_of_game(board)==0:
    display_board(board)
    moves=make_list_of_free_fields(board)
    if(moves==()):
        break
    print("List of possible moves:",moves)
    enter_move(board)
display_board(board)
state=state_of_game(board)
if state==0:
    print("It's a DRAW! Try again.")
elif state==1:
    print("Boo Hoo! You lose:(")
else:
    print("Congrats! You WIN!")
    