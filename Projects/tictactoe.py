import random

def drawBoard():
    print("    |  a  |  b  |  c  |")
    print("----+-----+-----+-----+")
    print(f"  1 |  {numtomark(B[0][0])}  |  {numtomark(B[0][1])}  |  {numtomark(B[0][2])}  |")
    print("----+-----+-----+-----+")
    print(f"  2 |  {numtomark(B[1][0])}  |  {numtomark(B[1][1])}  |  {numtomark(B[1][2])}  |")
    print("----+-----+-----+-----+")
    print(f"  3 |  {numtomark(B[2][0])}  |  {numtomark(B[2][1])}  |  {numtomark(B[2][2])}  |")
    print("----+-----+-----+-----+")

def numtomark(num):
    if num == 0:
        return " "
    elif num == 1:
        return "X"
    elif num == 2:
        return "O"

def checkwin():
    if B[0][0] == B[0][1] == B[0][2] != 0:
        return B[0][0]
    elif B[1][0] == B[1][1] == B[1][2] != 0:
        return B[1][0]
    elif B[2][0] == B[2][1] == B[2][2] != 0:
        return B[2][0]
    elif B[0][0] == B[1][0] == B[2][0] != 0:
        return B[0][0]
    elif B[0][1] == B[1][1] == B[2][1] != 0:
        return B[0][1]
    elif B[0][2] == B[1][2] == B[2][2] != 0:
        return B[0][2]
    elif B[0][0] == B[1][1] == B[2][2] != 0:
        return B[0][0]
    elif B[0][2] == B[1][1] == B[2][0] != 0:
        return B[0][2]
    else:
        for row in B:
            for cell in row:
                if cell == 0:
                    return 0
        return 3

def checkvalid(x, y):
    if x < 1 or x > 3 or y < 1 or y > 3:
        return False

    elif B[x - 1][y - 1] != 0:
        return False
    else:
        return True

def machineplay():
    while True:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if checkvalid(x, y):
            B[x - 1][y - 1] = 2
            break

def player_move():
    while True:
        inp = input("Your Move (Enter 00 to Exit)? ")
        if inp == "00":
            print("Thank You for Playing Tic-Tac-Toe")
            exit()
        x = int(inp[0])
        if inp[1] == 'a':
            y = 1
        elif inp[1] == 'b':
            y = 2
        elif inp[1] == 'c':
            y = 3
        else:
            x = 9
            y = 9
        if x == 9:
            print("Invalid Move. Try Again.")
            drawBoard()
            continue
        if checkvalid(x, y):
            B[x - 1][y - 1] = 1
            break
        else:
            if B[x - 1][y - 1] != 0:
                print("That cell is already full. Try Again.")
            else:
                print("Invalid Move. Try Again.")

            drawBoard()

def main():
    global B
    B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print("Welcome to Tic Tac Toe!")
    print("By Alp Dikmen")
    start = random.randint(1, 2)
    if start == 2:
        machineplay()
    while True:
        drawBoard()
        player_move()
        drawBoard()
        if checkwin() == 1:
            print("Congratulations. You Win!")
            break
        if checkwin() == 3:
            print("It's a tie!")
            break
        machineplay()
        if checkwin() == 2:
            drawBoard()
            print("Game Over. I Win!")
            break
        if checkwin() == 3:
            drawBoard()
            print("It's a tie!")
            break

main()