import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n, q = map(int, sys.stdin.readline().split())

arr = []

for _ in range(2**n):
    arr.append(list(map(int, sys.stdin.readline().split())))

q_list = list(map(int, sys.stdin.readline().split()))
visited = [[0]*(2**n) for _ in range(2**n)]

def bfs(n): #얼음 -1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()

    for i in range(2**n):
        for j in range(2**n):
            count = 0
            for k in range(4):
                a = i + dx[k]
                b = j + dy[k]

                if 0 <= a < 2**n and 0 <= b < 2**n:
                    if arr[a][b] > 0:
                        count += 1

            if count < 3:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        if arr[x][y] > 0:
            arr[x][y] -= 1

def bfs_1(queue, n): #최대 조각 개수 찾기
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    count = 0

    while queue:
        count += 1
        x, y = queue.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a < 2**n and 0 <= b < 2**n and visited[a][b] == 0:
                if arr[a][b] > 0:
                    queue.append((a, b))
                    visited[a][b] = 1

    return count

for m in range(q):
    temp = [[0] * (2 ** n) for _ in range(2 ** n)]
    for i in range(0, 2 ** n, 2 ** q_list[m]): #90도 회전시키는 알고리즘(복잡하다) 핵심은 좌표이동은 나중에 하기.
        for j in range(0, 2 ** n, 2 ** q_list[m]):
            for k in range(2 ** q_list[m]):
                for l in range(2 ** q_list[m]):
                    temp[l + i][2**q_list[m] - k - 1 + j] = arr[k + i][l + j]
    arr = temp
    bfs(n)

count = 0

for i in range(2**n):
    for j in range(2**n):
        queue1 = deque()
        if visited[i][j] == 0 and arr[i][j] > 0:
            queue1.append((i, j))
            visited[i][j] = 1
            count = max(count, bfs_1(queue1, n))

result = 0
for i in range(2**n):
    result += sum(arr[i])

print(result)
print(count)
