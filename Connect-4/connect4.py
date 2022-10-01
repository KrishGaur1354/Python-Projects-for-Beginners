#Dependencies
from os import system,name
import random

#Functions
def clear():
    if(name=='nt'): system('cls')
    else: system('clear')
def intro():
    print('Welcome to Connect-4')
    print('Token Distribution: ')
    print('Player 1: ',tok[0])
    print('Player 2: ',tok[1],end='')
    if(mode):
        print(' (Computer)')
    input('\nPress Enter to Start.')
def drawGrid(arr):
    for i in range(1,8):
        print(i,end=' ')
    print('\n'+('--'*7))
    for i in range(6):
        for j in range(7):
            print(arr[i][j],end=' ')
        print()      
def insert(arr):
    y = 0
    while(True):
        if(mode and count%2): 
            y = comp(arr)
            break
        y = int(input('Enter column number: '))
        y -= 1
        if(y<0 or y>6 or arr[0][y]!='*'):
            print('! Invalid Input !\n')
        else: 
            break
    col = 6
    while(col):
        if(arr[col-1][y]=='*'):
            arr[col-1][y] = token
            break
        col -= 1
def hCheck(token):
    for i in range(6):
        count = 0
        for j in range(7):
            if(arr[i][j]==token): count += 1
            else: count = 0
            if(count==4): return token
    return 0
def vCheck(token):
    for i in range(7):
        count = 0
        for j in range(6):
            if(arr[j][i]==token): count += 1
            else: count = 0
            if(count==4): return token
    return 0
def majdCheck(token):
    for i in range(3):
        for j in range(4):
            count,len = 0,4
            while(len):
                if(arr[i+len-1][j+len-1]==token): count += 1
                else: count = 0
                len -= 1
            if(count==4): return token
    return 0
def mindCheck(token):
    for i in range(3):
        for j in range(3,7):
            count,len = 0,4
            while(len):
                if(arr[i+len-1][j-len+1]==token): count += 1
                else: count = 0
                len -= 1
            if(count==4): return token
    return 0
def comp(arr):
    moves = []
    for i in range(0,7):
        if(arr[0][i]=='*'):
            moves.append(i)
    return random.choice(moves)

#Main Program
arr = [['*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*']]
tok = ['#','$']
count  = 42
mode = int(input("0: Multiplayer\n1: Single Player\nSelect Game mode : "))
intro()

#Game Loop
while(count):
    clear()
    token = tok[count%2]
    drawGrid(arr)
    print('Player ',tok.index(token)+1,'\'s chance.')
    insert(arr)
    if(hCheck(token) or vCheck(token) or majdCheck(token) or mindCheck(token)):
        clear()
        drawGrid(arr)
        print('Player ',tok.index(token)+1,' is the Winner \U0001F973\U0001F389')
        break
    count -= 1
if(count==0):
    print('It was a Draw. LOL!\nBoth of you lost.\n')
if(input('Press any key to exit.')):
    clear()
    exit()