import colorama
from colorama import Fore , Style
import random
import datetime

def show_game_board():
    for i in range(3):
        for j in range(3):
            print(game[i][j] , end = ' ')
            print(Style.RESET_ALL , end = ' ')
        print()

def exit_play():
    finish = datetime.datetime.now()
    time = finish - start
    print(int(time.total_seconds() * 1000))
    exit()

def check():
    for i in range(3):
        if game[i][0] == 'X' and game[i][1] == 'X' and game[i][2]== 'X':
            print('Player1 Win! ')
            exit_play()
        if game[i][0] == 'O' and game[i][1] == 'O' and game[i][2]== 'O':
            print('Player2 Win! ')
            exit_play()
    for j in range(3):
        if game[0][j] == 'X' and game[1][j] == 'X' and game[2][j]== 'X':
            print('Player1 Win! ')
            exit_play()
        if game[0][j] == 'O' and game[1][j] == 'O' and game[2][j]== 'O':
            print('Player2 Win! ')
            exit_play()     
    for i in range(3):
        for j in range(3):
            if i==j and game[i][j]== 'X':
                print('Player1 Win! ')
                exit_play()
            if i==j and game[i][j] == 'O':
                print('Player2 Win! ')
                exit_play()
    if game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X':
        print('Player1 Win! ')
        exit_play()
    if game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O':
        print('Player2 Win! ')
        exit_play()
    if rand == 9:
        print('No Win! ')
        exit_play()

def check_player1():
    while True:
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == '_':
                game[row][col] = Fore.RED + 'X'
                break
            else:
                print('Cell is not empty! ')
        else:
            print('Index is out of range! Try again: ')

def check_player2():
    while True:
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == '_':
                game[row][col] = Fore.BLUE + 'O'
                break
            else:
                print('Cell is not empty! ')
        else:
            print('Index is out of range! Try again: ')

def check_system():
    while True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == '_':
                game[row][col] = Fore.BLUE + 'O'
                break
            else:
                print('Cell is not empty! ')
        else:
            print('Index is out of range! Try again: ')

game = [['_' , '_' , '_'] ,
        ['_' , '_' , '_'] , 
        ['_' , '_' , '_']]
show_game_board()

while True:
    print('Choose which one: ')
    print('1- Player1 and Player2 ')
    print('2- Player1 and System ')
    n = int(input('Please enter your choice: '))
    rand = 0
    if n == 1:
        start = datetime.datetime.now()
        while True:
            print('Player1: ')
            check_player1()
            rand += 1
            show_game_board()
            check()
            print('Player2: ')
            check_player2()
            rand += 1
            show_game_board()
            check()
    if n == 2:
        start = datetime.datetime.now()
        while True:
            print('Player1: ')
            check_player1()
            rand += 1
            show_game_board()
            check()
            print('System: ')
            check_system()
            rand += 1
            show_game_board()
            check()