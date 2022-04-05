import sys

# 아래 코드 개선
# if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
#     1
#
# if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
#     w(20, 20, 20)
#
# if a < b and b < c, then w(a, b, c) returns:
#     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#
# otherwise it returns:
#     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

# 메모이제이션 (memoization)으로 dp값 저장하여 재귀호출 횟수를 줄인다.
read = sys.stdin.readline
dp = [ [[0] * 21 for _ in range(21) ] for _ in range(21) ]

def w(a,b,c):
    if a<=0 or b<= 0 or c<= 0:
        return 1
    if a > 20 or b > 20 or c > 20 :
        return w(20,20,20)

    if dp[a][b][c]:
        return dp[a][b][c]
    else:
        if a < b < c :
            dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
            return dp[a][b][c]
        else:
            dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
            return dp[a][b][c]



while True:
    a,b,c = map(int,read().split())
    if a == -1 and b == -1 and c == -1 :
        break

    else:
        answer = w(a,b,c)
        print('w(%d, %d, %d) = %d' %(a,b,c,answer ))
