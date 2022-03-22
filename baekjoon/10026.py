#적록색약
from collections import deque

n = int(input())

arr = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[0]*n for _ in range(n)] #방문한 node인가

for i in range(n):
	arr.append(list(input()))

def bfs(x, y, color):
	queue = deque()
	queue.append((x,y))

	while queue:
		x, y = queue.popleft()

		if visited[x][y] == 0:  #방문 안한 곳만 탐색을 해야함.
			visited[x][y] = 1 #탐색했다고 update

			for i in range(4):
				a = x + dx[i]
				b = y + dy[i]

				if 0 <= a < n and 0 <= b < n:
					if arr[a][b] == color: #color 가 같은 경우에만 확장
						queue.append((a,b))

count1 = 0
for i in range(n): #적록색맹 아닌 경우
	for j in range(n):
		if visited[i][j] == 0:
			color = arr[i][j]
			bfs(i, j, color)
			count1 += 1

visited = [[0]*n for _ in range(n)] #배열 초기화

for i in range(n): #R을 전부 G로 바꿔줌
	for j in range(n):
		if arr[i][j] == 'R':
			arr[i][j] = 'G'

count2 = 0
for i in range(n): #적록색맹인 경우
	for j in range(n):
		if visited[i][j] == 0:
			color = arr[i][j]
			bfs(i, j, color)
			count2 += 1

print(count1, count2)