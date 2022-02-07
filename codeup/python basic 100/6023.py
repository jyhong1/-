a = input()
flag = 0
for i in range(0, len(a)):
	if(a[i]==':' and flag == 0):
		b = i
		flag = 1
	if(a[i]==':' and flag==1):
		c = i

print(a[b+1:c])

#모범답안은 split(:) 이용해서 따로 입력하는것.
