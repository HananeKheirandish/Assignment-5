from colorama import Fore,Style
import datetime

def show_game_board():
    for i in range(3):
        for j in range(3):
            #if game[i][j] == 'X':
                #print(Fore.RED + 'X')
            #elif game[i][j] == 'O':
                #print(Fore.BLUE + 'O')
            #else:
            print(game[i][j] , end = ' ')
            print(Style.RESET_ALL , end = '')
        print()

def check():
    #for i in range(3):
        #win = 0
        #for j in range(3):
            #if game[i][j] == 'X':
               #win += 1 
            #elif game[i][j] == 'O':
                #win += 1
    #if win == 3 and game[i][j]=='X':
        #print('Player1 Win! ')
    #elif win == 3 and game[i][j] == 'o':
        #print('Player2 Win! ')
    win1 = 0
    win2 = 0
    if (game[0][0] == 'X' and game[0][1] == 'X' and game[0][2] == 'X') or (game[1][0] == 'X' and game[1][1] == 'X' and game[1][2] == 'X') or (game[2][0] == 'X' and game[2][1] == 'X' and game[2][2] == 'X'):
        win1 +=1
        #exit
    if (game[0][0] == 'O' and game[0][1] == 'O' and game[0][2] == 'O') or (game[1][0] == 'O' and game[1][1] == 'O' and game[1][2] == 'O') or (game[2][0] == 'O' and game[2][1] == 'O' and game[2][2] == 'O'):
        win2 += 1
        #exit
    if (game[0][0] == 'X' and game[1][0] == 'X' and game[2][0] == 'X') or (game[0][1] == 'X' and game[1][1] == 'X' and game[2][1] == 'X') or (game[0][2] == 'X' and game[1][2] == 'X' and game[2][2] == 'X'):
        win1 +=1
    if (game[0][0] == 'O' and game[1][0] == 'O' and game[2][0] == 'o') or (game[0][1] == 'O' and game[1][1] == 'O' and game[2][1] == 'O') or (game[0][2] == 'O' and game[1][2] == 'O' and game[2][2] == 'O'):
        win2 +=1
    if (game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X'):
        win1 += 1
    if (game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O'):
        win2 += 1
    if (game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X'):
        win1 += 1
    if (game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O'):
        win2 += 1
    #for i in range(3):
        #for j in range(3):
            #if i==j and game[i][j] == 'X':
                #win1 += 1
                #exit
            #if i==j and game[i][j] == 'O':
                #win2 += 1
                #exit
    finish = datetime.datetime.now()
    time = start - finish
    if win1 > win2:
        print('player1 win! ')
        print(int(time.total_seconds() * 1000))
        exit
    elif win2>win1:
        print('player2 win! ')
        print(int(time.total_seconds() * 1000))
        exit
    elif win1 == win2 == 0:
        print('no win!')
        print(int(time.total_seconds() * 1000))
        exit
    else:
        print('players same! ')
        print(int(time.total_seconds() * 1000))
        exit

game = [['_','_','_'] ,
        ['_','_','_'] , 
        ['_','_','_']]
show_game_board()

while True:
    print('choose which one: ')
    print('1-player1 and player2')
    print('2-player1 and system')
    n = int(input('your choose: '))
    if n==1:
        start = datetime.datetime.now()
        while True:
            print('player1: ')
            while True:
                row = int(input('please enter row: '))
                col = int(input('please enter column: '))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if game[row][col] == '_':
                        game[row][col] = Fore.RED+'X'
                        break
                    else:
                        print('cell is not empty! ')
                else:
                    print('Index is out of range! Try again: ')
            show_game_board()
            print('player2: ')
            while True:
                row = int(input('please enter row: '))
                col = int(input('please enter column: '))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if game[row][col] == '_':
                        game[row][col] = Fore.BLUE+'O'
                        break
                    else:
                        print('cell is not empty! ')
                else:
                    print('Index is out of range! Try again: ')
            show_game_board()
            check()