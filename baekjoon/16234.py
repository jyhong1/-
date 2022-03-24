#인구이동 시간 초과때문에 빡세서 python 말고 pypy3 으로 제출

from collections import deque

n, l, r = map(int, input().split())

arr = []
visited = [[0]*n for _ in range(n)]
isTrue = False

for i in range(n):
	arr.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0

def bfs(x, y):
	temp = []
	count = 1
	queue = deque()
	queue.append((x, y))
	people = arr[x][y]
	global isTrue
	visited[x][y] = 1 #방문한 것 바로 update

	temp.append([x, y])

	while queue:
		#print(queue)
		x,y = queue.popleft()

		for i in range(4):
			a = x + dx[i]
			b = y + dy[i]

			if 0 <= a < n and 0 <= b < n and visited[a][b] == 0:
				if l <= abs(arr[x][y] - arr[a][b]) <= r: #조건에 따라 temp 에 추가해주고 바로 average 구함.
					queue.append((a, b))
					temp.append([a, b])
					visited[a][b] = 1
					count += 1
					people += arr[a][b]

	people_avg = int(people / count)

	if len(temp) > 1: # temp 의 크기가 1 보다 커야 이동이 일어난다. 
		isTrue = True
		for x, y in temp:
			arr[x][y] = people_avg

while True: #핵심이라고 볼 수 있는 부분? 인구 이동이 일어나면 일어나지 않을때까지 for문 돌려야함(isTrue 변수로)
	result = 0 
	visited = [[0]*n for _ in range(n)]
	isTrue = False
	for i in range(n):
		for j in range(n):
			if visited[i][j] == 0:
				bfs(i, j)

	if isTrue == False:
		break
	count += 1

print(count)