# function where main work is being done
def tictactoe(a,b):
    win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]] #list of possible winning conditions

    player1=[] # lists for player inputs
    player2=[]

    grid = [' ',' ',' ',' ',' ',' ',' ',' ',' '] #this list will contain the symbols corresponding to positions of 2D grid

    print(" 7 | 8 | 9 \n___|___|___\n 4 | 5 | 6 \n___|___|___\n 1 | 2 | 3 ") #grid layout printing section

    exit_flag=False
    counter = 1

    print("Game will start with player 1 \n\n") #beginning the game now

    while counter<=9 and exit_flag==False: #conditions : when moves are not greater than 9 or when exit_flag is not true

        position = int(input("Enter the position on grid for player: "))

        if counter%2 == 1 and grid[position-1] == " ":
            grid[position-1] = a
            player1.append(position) #creating list of locations where player1 has put his marker
            counter += 1
        elif counter%2 == 0 and grid[position-1] == " ":
            grid[position-1]=b
            player2.append(position) #creating list of locations where player1 has put his marker
            counter += 1
        else:
        	continue

        #printing the grid along with markers in it
        print(f" {grid[6]} | {grid[7]} | {grid[8]} \n___|___|___\n {grid[3]} | {grid[4]} | {grid[5]} \n___|___|___\n {grid[0]} | {grid[1]} | {grid[2]} ")

        if counter >= 5:
            if (counter - 1) % 2 == 1:
                for i in win: #for accessing nested list win from line 2, for example [[1,2,3],[4,5,6],.....]
                    flag = True
                    for j in i: #for accessing nested list individual elements, for example 1,2,3 in [[1,2,3]....]
                        if j in player1: 
                            flag = True
                        else:
                            flag = False
                            break
                    if flag == True:
                        print("\nPlayer 1 won\n")
                        exit_flag = True
                        break
            else:
                for i in win:
                    flag = True
                    for j in i:
                        if j in player2:
                            flag = True
                        else:
                            flag = False
                            break
                    if flag == True:
                        print("\nPlayer 2 won\n")
                        exit_flag = True
                        break
    if counter > 9:
        print("Draw\n")

# Calling part of the code
print("Welcome to Tic Tac Toe\n")
answer = input("Do you want to begin the game?YES/NO ")
if answer == "YES":
    print("Kindly choose the symbols for:\n")
    a = input("Player 1 ")
    b = input("Player 2 ")
while answer == "YES":
    tictactoe(a,b)
    answer=input("Do you want to play again? YES/NO ")
    
print("Thank You, Bye Bye")
            
            