def sum(a, b, c ):
    return a + b + c


def printBoard(playerX, playerY):
    zero = 'X' if playerX[0] else ('O' if playerY[0] else 0)
    one = 'X' if playerX[1] else ('O' if playerY[1] else 1)
    two = 'X' if playerX[2] else ('O' if playerY[2] else 2)
    three = 'X' if playerX[3] else ('O' if playerY[3] else 3)
    four = 'X' if playerX[4] else ('O' if playerY[4] else 4)
    five = 'X' if playerX[5] else ('O' if playerY[5] else 5)
    six = 'X' if playerX[6] else ('O' if playerY[6] else 6)
    seven = 'X' if playerX[7] else ('O' if playerY[7] else 7)
    eight = 'X' if playerX[8] else ('O' if playerY[8] else 8)
    print(f"| {zero} | {one} | {two}  |")
    print(f"|--|---|--|")
    print(f"| {three} | {four} | {five} |")
    print(f"|--|---|--|")
    print(f"| {six} | {seven} | {eight} |") 


def checkwinner(playerX, playerY):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(playerX[win[0]], playerX[win[1]], playerX[win[2]]) == 3):
            print("Player X has won the game")
            return 1
        if(sum(playerY[win[0]], playerY[win[1]], playerY[win[2]]) == 3):
            print("Player Y has won the game")
            return 0
    return -1
        

if __name__ == "__main__":
    playerX = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    playerY = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Tic-Tac-Toe")
    while(True):
        printBoard(playerX, playerY)
        if(turn == 1):
            print("X's Chance to Play")
            value = int(input("Enter your Value: "))
            playerX[value] = 1
        else:
            print("O's Chance to Play")
            value = int(input("Enter your Value: "))
            playerY[value] = 1

        winner = checkwinner(playerX, playerY)
        if(winner != -1):
            print("Match Over")
            break

        turn = 1 - turn
                
