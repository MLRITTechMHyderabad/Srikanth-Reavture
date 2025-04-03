# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 14:57:03 2025

@author: 91766
"""
"""
import random
R=int(input("enter no of rounds:"))
rows, cols = 3, 4
matrix = [[0] * cols for _ in range(rows)]
for i in range(len(matrix)):
    for j in range(i,len(matrix[i])):
        x=random.randint(1, 7)
        matrix[i][j]=x
        
#=random.randomint(1,7)
print(matrix)

for i in range(1,7):
    count=0
    for j in range(1,7):
        if i+j==8:
            count=count+1
            
print(count)
"""

def dicegame(player1, player2):

    count1,count2 = 0,0
    for i in range(len(player1)):
        if sum(player1[i])/ 36 > sum(player2[i])/36:
            count1 += 1
        elif sum(player1[i])/36 < sum(player2[i])/36:
            count2 += 1
        else:
            count1 += 1
            count2 += 1
    if count1 > count2:
        return("Player1")
    elif count2 > count1:
        return("Player2")
    else:
        return("Draw")
# 3
# 1 1 3 4
# 2 2 6 6
# 5 3 4 6
n = int(input("enter the rounds of game"))
player1 = [[0,0] for i in range(n)]
player2 = [[0,0] for i in range(n)]
for i in range(n):
    s = input()
    a = list(map(int, s.split()))
    for j in range(len(a)):
        if a[j] > 6 or a[j] < 0:
            a[j] = 0
    player1[i][0] = a[0]
    player1[i][1] = a[1]
    player2[i][0] = a[2]
    player2[i][1] = a[3]
print(dicegame(player1, player2))