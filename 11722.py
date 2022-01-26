import sys
from bisect import bisect_left
read = sys.stdin.readline

n = int(read())
A = [0]+ list(map(int, read().split()))

dp =[0] * (n+1)
tmp = [0]

for i in range(1,n+1):
    if A[i] > tmp[-1]:
        tmp.append(A[i])
        dp[i] = len(tmp)-1
    else:
        dp[i] = bisect_left(tmp,A[i])
        tmp[dp[i]] = A[i]
print(max(dp))

