def removeKDigits(num, k):
	size = len(num)
	if size == k:
		return "0"
	stack = []
	i=0
	while i < size:
		## Greedy Approach
		while k > 0 and len(stack) != 0 and stack[-1] > num[i]:
			stack.pop()
			k-=1
	
		stack.append(num[i])
		i+=1
	while k > 0:
		stack.pop()
		k-=1
		
	return "".join(stack)


num = input()
k = int(input())
n = removeKDigits(num, k)
print(n)