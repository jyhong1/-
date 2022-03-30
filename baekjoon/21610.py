#마법사 상어와 비바라기
from collections import deque

n, m = map(int, input().split())

arr = []
move = []

for _ in range(n):
	arr.append(list(map(int, input().split())))

for _ in range(m):
	move.append(list(map(int, input().split())))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dx_diag = [1, 1, -1, -1]
dy_diag = [1, -1, 1, -1]

queue = deque()
queue.append((n-1, 0))
queue.append((n-1, 1))
queue.append((n-2, 0))
queue.append((n-2, 1))

def attack(d, s):
	visited = [[0]*n for _ in range(n)]
	for i in range(len(queue)): #구름 이동
		x, y = queue.popleft()

		x = x + s * dx[d-1]
		y = y + s * dy[d-1]

		x = (x + n) % n
		y = (y + n) % n

		queue.append((x, y))
		arr[x][y] += 1
		visited[x][y] = 1

	for i in range(len(queue)):
		x, y = queue[i]
		count = 0
		for i in range(4):
			a = x + dx_diag[i]
			b = y + dy_diag[i]

			if 0 <= a < n and 0 <= b < n and arr[a][b] > 0:
				count += 1
		
		arr[x][y] += count

	queue.clear()
	
	for i in range(n):
		for j in range(n):
			if visited[i][j] == 0 and arr[i][j] >= 2: 
					arr[i][j] -= 2
					queue.append((i, j))


for i in range(m):	
	attack(move[i][0], move[i][1])

result = 0
for i in range(n):
	result += sum(arr[i])

print(result)