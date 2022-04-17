#컨베이어 벨트 위의 로봇
from collections import deque

n, k = map(int, input().split())

arr = list(map(int, input().split()))
robot = [0 for _ in range(2*n)]

process = 1
a = 0
b = n-1

queue = deque()

while(1):
    index = -1 #index 초기화 위치 중요함.
    count = 0
    a = (a-1+(2*n))%(2*n) #+1 이 아닌 -1 을 해줘야 함.
    b = (b-1+(2*n))%(2*n)

    if(robot[b]==1): #이동하였을때 제거할 것은 해줘야함.
        robot[b] = 0
        queue.remove(b)

    if len(queue) > 0:
        for i in range(len(queue)):
            x = queue[i]
            if arr[(x+1)%(2*n)] >= 1 and robot[(x+1)%(2*n)] == 0:
                robot[x] = 0
                robot[(x+1)%(2*n)] = 1
                arr[(x+1)%(2*n)] -= 1
                queue[i] = (x+1)%(2*n)
                
                if (x+1)%(2*n) == b and robot[(x+1)%(2*n)] == 1: 
                    #미리 remove 하게 되면, queue order가 흐트러지므로 index에 저장 후 나중에 remove
                    index = (x+1)%(2*n)

    if(index >= 0):
        queue.remove(index)
        robot[index] = 0
    
    if arr[a] >= 1:
        robot[a] = 1
        queue.append(a)
        arr[a] -= 1

    for i in range(2*n):
        if arr[i] == 0:
            count += 1
    
    if count >= k:
        print(process)
        break

    process += 1