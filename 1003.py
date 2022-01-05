import sys
read = sys.stdin.readline

# 피보나치 수열의 0과 1의 호출 개수를 구하는 문제로
# 기존 피보나치 dp로 구현하면 시간초과 발생함.
# fibo(n)수의 0,1의 갯수 = fibo(n-2)의 0,1의 갯수 + fibo(n-1)의 0,1의 갯수로 구하는 아이디어로 구현

cnt_zero = [1,0,1]
cnt_one = [0,1,1]

def fibonacci(num):
    length = len(cnt_zero)
    # 호출할 때 이전 값을 중복 계산하지 않기 위해 배열을 사용함
    if num >= length:
        for i in range(length, num+1):
            cnt_zero.append(cnt_zero[i-1] + cnt_zero[i-2])
            cnt_one.append(cnt_one[i-1] + cnt_one[i-2])
    print('{} {}'.format(cnt_zero[num], cnt_one[num]))

T = int(read())

for _ in range(T):
    fibonacci(int(read()))