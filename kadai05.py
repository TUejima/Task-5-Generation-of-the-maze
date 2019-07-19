# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create by KanameTakano
Date:2017/10/25
'''
import random
import sys

# 初期化
Length = 29
MazeSize = [[1 for i in range(Length)] for j in range(Length)]

if Length % 2 == 0:
    print("error 奇数のみ")
    sys.exit(1)

for i in range(1, Length - 1):
    for j in range(1, Length - 1):
        if i % 2 == 1:
            MazeSize[i][j] = 0
        else:
            if j % 2 == 1:
                MazeSize[i][j] = 0


# 迷路生成
for i in range(1, Length - 1):
    for j in range(1, Length - 1):

        if i % 2 == 0 and j % 2 == 0:
            ram = random.randint(0, 3)
            if ram == 0:
                # print("0")
                if MazeSize[i][j - 1] == 0:
                    MazeSize[i][j - 1] = 1
                elif MazeSize[i - 1][j] == 0:
                    MazeSize[i - 1][j] = 1
                elif MazeSize[i][j + 1] == 0:
                    MazeSize[i][j + 1] = 1
                elif MazeSize[i + 1][j] == 0:
                    MazeSize[i + 1][j] = 1

            elif ram == 1:
                # print("1")
                if MazeSize[i - 1][j] == 0:
                    MazeSize[i - 1][1] = 1
                elif MazeSize[i][j + 1] == 0:
                    MazeSize[i][j + 1] = 1
                elif MazeSize[i + 1][j] == 0:
                    MazeSize[i + 1][j] = 1
                elif MazeSize[i][j - 1] == 0:
                    MazeSize[i][j - 1] = 1

            elif ram == 2:
                # print("2")
                if MazeSize[i][j + 1] == 0:
                    MazeSize[i][j + 1] == 1
                elif MazeSize[i + 1][j] == 0:
                    MazeSize[i + 1][j] = 1
                elif MazeSize[i][j - 1] == 0:
                    MazeSize[i][j - 1] = 1
                elif MazeSize[i - 1][j] == 0:
                    MazeSize[i - 1][j] = 1

            elif ram == 3:
                # print("3")
                if MazeSize[i + 1][j] == 0:
                    MazeSize[i + 1][j] = 1
                elif MazeSize[i][j - 1] == 0:
                    MazeSize[i][j - 1] = 1
                elif MazeSize[i - 1][j] == 0:
                    MazeSize[i - 1][j] = 1
                elif MazeSize[i][j + 1] == 0:
                    MazeSize[i][j + 1] = 1

            else:
                print("ramdom error")
                sys.exit(1)

# startとgoalの設定
# start
MazeSize[1][1] = 2
# goal
MazeSize[Length - 2][Length - 2] = 3

# 表示
print("○:Start")
print("●:Goal")
for Maze in MazeSize:
    for MazeChild in Maze:
        if MazeChild == 0:
            print("　", end="")

        elif MazeChild == 1:
            print("■", end="")

        elif MazeChild == 2:
            print("○", end="")

        elif MazeChild == 3:
            print("●", end="")
    print()
    # 改行
