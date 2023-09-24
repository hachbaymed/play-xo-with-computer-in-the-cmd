import os
import random
import time
from os import system
os.system('cls')
os.system('color 9f')
xo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print('+------+-----+-----+')
for i in xo:
    print('|      |     |     |')
    print("| ", end="  ")
    for j in i:
        print(j, end="  |  ")
    print()

    print('|      |     |     |')
    print('+------+-----+-----+')
win = False
c = 0
while True:
    n1 = 0
    while n1 not in xo[0] and n1 not in xo[1] and n1 not in xo[2]:
        n1 = int(input("Choisir un nombre :"))
        c += 1
    for i in range(3):
        for j in range(3):
            if xo[i][j] == n1:
                xo[i][j] = "O"
    os.system('cls')
    print('+------+-----+-----+')
    for i in xo:
        print('|      |     |     |')
        print("| ", end="  ")
        for j in i:
            print(j, end="  |  ")
        print()

        print('|      |     |     |')
        print('+------+-----+-----+')
    for i in range(3):
        if xo[0][i] == xo[1][i] == xo[2][i] or xo[i][0] == xo[i][1] == xo[i][2] or xo[0][0] == xo[1][1] == xo[2][2] or xo[0][2] == xo[1][1] == xo[2][0]:
            os.system('color 2f')
            print("Vous avez ganer")
            win = True
            break
    if win:
        break
    n2List = []
    for i in xo:
        for j in i:
            n2List.append(j)
    if c >= 9:
        if c >= 9:
            os.system('color 0f')
            print("Match nul")
            break
    n2 = True
    while type(n2) != int:
        n2 = random.choice(n2List)
    # Dificile conditions
    for i in range(3):
        if xo[i][0] == xo[i][1]:
            if type(xo[i][2]) == int:
                n2 = xo[i][2]
        elif xo[i][0] == xo[i][2]:
            if type(xo[i][1]) == int:
                n2 = xo[i][1]
        elif xo[i][1] == xo[i][2]:
            if type(xo[i][0]) == int:
                n2 = xo[i][0]
        if xo[0][i] == xo[1][i]:
            if type(xo[2][i]) == int:
                n2 = xo[2][i]
        elif xo[0][i] == xo[2][i]:
            if type(xo[1][i]) == int:
                n2 = xo[1][i]
        elif xo[1][i] == xo[2][i]:
            if type(xo[0][i]) == int:
                n2 = xo[0][i]
        else:
            if type(xo[1][1]) == int:
                n2 = xo[1][1]
    if xo[0][0] == xo[1][1]:
        if type(xo[2][2]) == int:
            n2 = xo[2][2]
    elif xo[2][2] == xo[1][1]:
        if type(xo[0][0]) == int:
            n2 = xo[0][0]
    elif xo[0][2] == xo[1][1]:
        if type(xo[2][0]) == int:
            n2 = xo[2][0]
    elif xo[2][0] == xo[1][1]:
        if type(xo[0][2]) == int:
            n2 = xo[0][2]
    for i in range(3):
        for j in range(3):
            if xo[i][j] == n2:
                xo[i][j] = "X"
                c += 1
    time.sleep(1)
    os.system('cls')
    print('+------+-----+-----+')
    for i in xo:
        print('|      |     |     |')
        print("| ", end="  ")
        for j in i:
            print(j, end="  |  ")
        print()

        print('|      |     |     |')
        print('+------+-----+-----+')
    for i in range(3):
        if xo[0][i] == xo[1][i] == xo[2][i] or xo[i][0] == xo[i][1] == xo[i][2] or xo[0][0] == xo[1][1] == xo[2][2] or xo[0][2] == xo[1][1] == xo[2][0]:
            os.system('color 4f')
            print("Game Over")
            win = True
            break
    if win:
        break
input()
