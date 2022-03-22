# 아기상어2
from collections import deque

n, m = map(int, input().split())

#initialize
arr = []
queue = deque()

#이동방향
dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 0, 1, -1, 0, 1, -1 ]

for i in range(n): #2차원 배열 input
	temp = list(map(int, input().split()))

	for j in range(m): #1인 부분을 queue에 저장
		if temp[j] == 1:
			queue.append((i, j))

	arr.append(temp)

def bfs():
	while queue:
		x, y = queue.popleft()

		for i in range(8):
			a = x + dx[i]
			b = y + dy[i]

			if 0 <= a < n and 0 <= b < m:
				if arr[a][b] == 0:
					queue.append((a,b)) #핵심
					arr[a][b] = arr[x][y] + 1

bfs()

answer = 0

for i in range(len(arr)):
	answer = max(answer, max(arr[i]))

print(answer-1)
