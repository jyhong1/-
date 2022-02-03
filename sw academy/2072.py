#홀수만 더하기

T = int(input())

for test_case in range(1, T + 1):
	sum = 0

	a = list(map(int, input().split())) #테스트케이스 받는 핵심 코드
		
	for i in a:
		if i%2 == 1:
			sum += i

	print('#' + str(test_case) + ' ' + str(sum)) #문자열이랑 같이 print 하려면 str로 바꿔줘야함