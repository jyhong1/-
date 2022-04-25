import sys
from collections import deque

sys.stdin = open("in.txt", "r")

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda arr: arr[1])
#print(arr)
p = [-1 for _ in range(n)]
opt = [0 for _ in range(n)]

'''
def init_p(n):
    for i in range(1, n):
    '''

#init_p(n)
#print(p)
for i in range(n):
    if i==0:
        opt[i] = arr[i][2]
    else:
        for j in range(i-1, -1, -1):
            if arr[i][0] > arr[j][1]:
                p[i] = j
                break
        if p[i] == -1:
            value = 0
        else:
            value = opt[p[i]]
        opt[i] = max(arr[i][2] + value, opt[i-1])
    print(f'opt[{i}]:{opt[i]}')

print(opt[n-1])

"""test case
8
1 3 3
2 4 2
1 5 4
4 6 1
5 7 2
4 9 5
6 10 2
9 10 1

4
2 4 4
3 6 6
6 8 2
5 7 3
"""