n, x = map(int, input().split()) #int로 받으려면 map을 사용하면된다.

h = [0] * (n+1)
p = [0] * (n+1)

h[0] = 1
p[0] = 1

def count(n, x):
	if n==0:
		if x==0: return 0
		else: return 1
	elif x==1:
		return 0
	elif x <= 1 + h[n-1]:
		return count(n-1, x-1)
	elif x == 1 + h[n-1] + 1:
		return p[n-1] + 1
	elif x <= 1 + h[n-1] + 1 + h[n-1]:
		return p[n-1] + 1 + count(n-1, x-(1+h[n-1]+1))
	else:
		return p[n]

for i in range(1, n+1):
	h[i] = 1 + h[i-1] + 1 + h[i-1] + 1
	p[i] = p[i-1] + 1 + p[i-1]

print(count(n, x))

