import sys
read = sys.stdin.readline

n = int(read())

A = list(map(int,read().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
maxVal = max(dp)
answer = []
for i in range(n-1,-1,-1):
    if dp[i] == maxVal:
        answer.append(A[i])
        maxVal -= 1

print(*answer[::-1])