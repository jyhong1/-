#이차원 배열과 연산

import sys
from collections import deque

sys.stdin = open("C:\\Users\\hjy\\Desktop\\code-practice\\baekjoon\\input.txt", "r")

r, c, value = map(int, sys.stdin.readline().split())

arr = []
for _ in range(3):
    arr.append(list(map(int, sys.stdin.readline().split())))

for time in range(101): 
    arr_temp = []
    row = len(arr)
    col = len(arr[0])

    if row >= r and col >= c:
        if arr[r-1][c-1] == value:
            print(time)
            break
    if time == 100:
        print(-1)
        break
    
    flag = 0

    if len(arr) < len(arr[0]):
        arr_temp = [[0]*row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                arr_temp[j][i] = arr[i][j]
        
        arr = arr_temp.copy()
        arr_temp = []
        flag = 1
 
    max_length = 0

    for k in arr:
        temp = []
        max_value = max(k)

        for i in range(1, max_value + 1):
            if k.count(i): temp.append([i, k.count(i)])

        temp = sorted(temp, key=lambda temp: temp[1])

        temp_temp = []
        for j in temp:
            temp_temp.append(j[0])
            temp_temp.append(j[1])

        temp_temp = temp_temp[:101]

        max_length = max(max_length, len(temp_temp))
        arr_temp.append(temp_temp)

    for i in range(len(arr_temp)):
        num = max_length - len(arr_temp[i])
        
        for j in range(num):
            arr_temp[i].append(0)

    if flag == 1:
        tmp = []
        row = len(arr_temp)
        col = len(arr_temp[0])

        tmp = [[0]*row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                tmp[j][i] = arr_temp[i][j]
        
        arr = tmp.copy()
        tmp = []
        
    if flag == 0: arr = arr_temp.copy()