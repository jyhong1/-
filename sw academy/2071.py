#평균값 구하기

T = int(input())

for test_case in range(1, T+1):
	sum = 0
	a = list(map(int, input().split()))

	for i in a:
		sum += i
	
	avg = sum / len(a)
	avg = round(avg, 0)
	avg = int(avg)

	print('#' + str(test_case) + ' ' + str(avg))


