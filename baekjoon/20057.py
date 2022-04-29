#마법사 상어와 토네이도 #not solved(hard)
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

left = [[0,0,2,0,0], [0,10,7,1,0], [5,0,0,0,0], [0,10,7,1,0], [0,0,2,0,0]]

def rotate(arr):
    arr2 = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            arr2[4-j][i] = arr[i][j]

    return arr2

down = rotate(left)
right = rotate(down)
up = rotate(right)

dx = []
dy = []

def tor(direct, x, y):
    out = 0

    if direct == 1: #left
        y -= 1
        y_value = arr[x][y]
        sand = 0
        sum = 0
        alpha = 0

        for i in range(-2, 3):
            for j in range(-2, 3):
                if 0 <= x + i < n and 0 <= y + j < n:
                    sand = int(y_value * left[i+2][j+2] / 100)
                    arr[x + i][y + j] += sand
                    sum += sand

                else:
                    sand = int(y_value * left[i + 2][j + 2] / 100)
                    out += sand

        alpha = y_value - sum
        if 0 <= x < n and 0 <= y-1 < n:
            arr[x][y-1] = alpha
        else:
            out += alpha

        arr[x][y] = 0

    if direct == 2: #down
        x += 1
        y_value = arr[x][y]
        sand = 0
        sum = 0
        alpha = 0

        for i in range(-2, 3):
            for j in range(-2, 3):
                if 0 <= x + i < n and 0 <= y + j < n:
                    sand = int(y_value * down[i+2][j+2] / 100)
                    arr[x + i][y + j] += sand
                    sum += sand

                else:
                    sand = int(y_value * down[i + 2][j + 2] / 100)
                    out += sand

        alpha = y_value - sum
        if 0 <= x+1 < n and 0 <= y < n:
            arr[x+1][y] = alpha
        else:
            out += alpha

        arr[x][y] = 0

    if direct == 3: #right
        y += 1
        y_value = arr[x][y]
        sand = 0
        sum = 0
        alpha = 0

        for i in range(-2, 3):
            for j in range(-2, 3):
                if 0 <= x + i < n and 0 <= y + j < n:
                    sand = int(y_value * right[i+2][j+2] / 100)
                    arr[x + i][y + j] += sand
                    sum += sand

                else:
                    sand = int(y_value * right[i + 2][j + 2] / 100)
                    out += sand

        alpha = y_value - sum
        if 0 <= x < n and 0 <= y+1 < n:
            arr[x][y+1] = alpha
        else:
            out += alpha

        arr[x][y] = 0

    if direct == 4: #up
        x -= 1
        y_value = arr[x][y]
        sand = 0
        sum = 0
        alpha = 0

        for i in range(-2, 3):
            for j in range(-2, 3):
                if 0 <= x + i < n and 0 <= y + j < n:
                    sand = int(y_value * up[i+2][j+2] / 100)
                    arr[x + i][y + j] += sand
                    sum += sand

                else:
                    sand = int(y_value * up[i + 2][j + 2] / 100)
                    out += sand

        alpha = y_value - sum
        if 0 <= x-1 < n and 0 <= y < n:
            arr[x-1][y] = alpha
        else:
            out += alpha

        arr[x][y] = 0

    return x, y, out

result = 0
result_sum = 0
x, y = 2, 2

x,y, result = tor(1, x, y)
result_sum += result
x,y, result = tor(2, x, y)
result_sum += result

for i in range(2):
    x, y, result = tor(3, x, y)
    result_sum += result

for i in range(2):
    x, y, result = tor(4, x, y)
    result_sum += result

for i in range(3):
    x, y, result = tor(1, x, y)
    result_sum += result

for i in range(3):
    x, y, result = tor(2, x, y)
    result_sum += result

for i in range(4):
    x, y, result = tor(3, x, y)
    result_sum += result

for i in range(4):
    x, y, result = tor(4, x, y)
    result_sum += result

for i in range(4):
    x, y, result = tor(1, x, y)
    result_sum += result

print(result_sum)