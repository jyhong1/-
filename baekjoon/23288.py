# 주사위 굴리기 2

import sys
from collections import deque

#sys.stdin = open("input.txt", "r")

n, m, k = map(int, sys.stdin.readline().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dice = [2, 4, 1, 3, 5, 6]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
move = 0
x, y = 0, 0

result = 0


def roll_dice(d, dice):
    dice_temp = []

    d1 = dice[0]
    d2 = dice[1]
    d3 = dice[2]
    d4 = dice[3]
    d5 = dice[4]
    d6 = dice[5]

    if d == 0:  # east
        dice_temp = [d1, d6, d2, d3, d5, d4]

    elif d == 2: # west
        dice_temp = [d1, d3, d4, d6, d5, d2]

    elif d == 3: # north
        dice_temp = [d3, d2, d5, d4, d6, d1]

    else: # south
        dice_temp = [d6, d2, d1, d4, d3, d5]

    return dice_temp

def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    count = 1
    queue = deque()
    queue.append((x, y))

    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        val = arr[x][y]

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a < n and 0 <= b < m and val == arr[a][b] and visited[a][b] == 0:
                queue.append((a, b))
                visited[a][b] = 1
                count += 1
    return count

def next_coor(x, y, move, dice):
    dice1 = []
    move1 = 0
    if move == 0:
        if y+1 < m:
            dice1 = roll_dice(move, dice)
            y += 1
            move1 = move
        else:
            dice1 = roll_dice(2, dice)
            y -= 1
            move1 = 2

    elif move == 2:
        if y - 1 >= 0:
            dice1 = roll_dice(move, dice)
            y -= 1
            move1 = 2
        else:
            dice1 = roll_dice(0, dice)
            y += 1
            move1 = 0

    elif move == 3:
        if x - 1 >= 0:
            dice1 = roll_dice(move, dice)
            x -= 1
            move1 = 3
        else:
            dice1 = roll_dice(1, dice)
            x += 1
            move1 = 1

    elif move == 1:
        if x + 1 < n:
            dice1 = roll_dice(move, dice)
            x += 1
            move1 = 1
        else:
            dice1 = roll_dice(3, dice)
            x -= 1
            move1 = 3
    return x, y, dice1, move1

def where_to_roll(x, y, dice, move):
    if dice[5] > arr[x][y]:
        move1 = (move+1+4) % 4
    elif dice[5] < arr[x][y]:
        move1 = (move-1+4) % 4
    else:
        move1 = move
    return move1

for i in range(k):
    x, y, dice, move = next_coor(x, y, move, dice)
    result += bfs(x, y)*arr[x][y]
    move = where_to_roll(x, y, dice, move)

print(result)




