def findJudge(N, trust):
    trustValue = {}
    for i in range(1, N+1):
        trustValue[i] = 0
    for pair in trust:
        trustValue[pair[0]] -= 1
        trustValue[pair[1]] += 1
    for i in trustValue:
        if trustValue[i] == N-1:
            return i
    return -1
   
N = int(input())
trust = []
for i in range(N):
	trust.append(list(map(int, input().split(','))))
r = findJudge(N, trust)
print(r)