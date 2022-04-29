#마법사 상어와 파이어볼

import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n, m, k = map(int, sys.stdin.readline().split())

arr_temp = []
queue = deque()

for _ in range(m):
    queue.append(list(map(int, sys.stdin.readline().split())))

arr = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move(x, y, d, s, n):
    s = s % (n)
    x = x + (s * dx[d])
    y = y + (s * dy[d])

    return x % n, y % n

for T in range(k):

    while queue:
        x, y, m, s, d = queue.popleft()

        if T==0:
            a, b = move(x - 1, y - 1, d, s, n)
        else:
            a, b = move(x, y, d, s, n)
            arr[x][y].pop(0)

        arr[a][b].append([a, b, m, s, d])

    for i in range(n):
        for j in range(n):
            size = len(arr[i][j])
            if size >= 2:
                flag = 0
                mass = 0
                vel = 0
                direct = arr[i][j][0][4] % 2

                for k in arr[i][j]:
                    mass += k[2]
                    vel += k[3]
                    dir_temp = k[4] % 2

                    if not direct == dir_temp:
                        flag = 1

                mass = int(mass / 5)
                vel = int(vel / size)

                if flag == 0:
                    dir_arr = [0, 2, 4, 6]
                else:
                    dir_arr = [1, 3, 5, 7]

                arr[i][j].clear()

                if mass > 0:
                    for l in dir_arr:
                        arr[i][j].append([i, j, mass, vel, l])
                        queue.append([i, j, mass, vel, l])

            elif size == 1:
                queue.append([arr[i][j][0][0], arr[i][j][0][1], arr[i][j][0][2], arr[i][j][0][3], arr[i][j][0][4]])

result = 0
for i in range(n):
    for j in range(n):
        for k in arr[i][j]:
            result += k[2]

print(result)