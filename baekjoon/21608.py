#상어 초등학교
import sys
from collections import deque

#sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

arr = []
stu = [[0]*n for _ in range(n)] # 학생 배치

for _ in range(n**2):
    arr.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for k in range(n**2):
    stu_num = arr[k][0] # 입력할 학생의 번호

    count_like = 0
    count_blank = 0
    temp = []
    flag = 0

    for i in range(n):
        for j in range(n):
            count_like_temp = 0
            count_blank_temp = 0

            if stu[i][j] == 0:
                if flag == 0: #temp 초기화 필수
                    temp.append([i, j])
                    flag = 1

                for l in range(4):
                    a = i + dx[l]
                    b = j + dy[l]

                    if 0 <= a < n and 0 <= b < n:
                        if stu[a][b] in arr[k]: # 좋아하는 학생이 있을 때
                            count_like_temp += 1

                        if stu[a][b] == 0:
                            count_blank_temp += 1

            if count_like_temp > count_like:
                temp.clear()
                temp.append([i, j])
                count_like = count_like_temp
                count_blank = count_blank_temp

            elif count_like_temp == count_like:
                if count_blank_temp > count_blank:
                    temp.clear()
                    temp.append([i, j])
                    count_blank = count_blank_temp

    #print(temp)
    stu[temp[0][0]][temp[0][1]] = stu_num

#print(stu)

result = 0
arr_sort = sorted(arr, key=lambda arr: arr[0]) #특정 index로 sorting

for i in range(n):
    for j in range(n):
        count_like = 0
        stu_num = stu[i][j]

        for l in range(4):
            a = i + dx[l]
            b = j + dy[l]

            if 0 <= a < n and 0 <= b < n:
                if stu[a][b] in arr_sort[stu_num-1]:  # 좋아하는 학생이 있을 때
                    count_like += 1

        if count_like == 0:
            continue
        else:
            result += 10**(count_like - 1)

print(result)

