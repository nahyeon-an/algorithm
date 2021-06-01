"""
1947 : 선물 전달
"""
import sys

mod = 1000000000

n = int(sys.stdin.readline().strip())

if n == 1:
    print(0)
    sys.exit(0)
elif n == 2:
    print(1)
    sys.exit(0)

# dp[i] : i명이 선물을 나누어 가지는 경우의 수
# 인덱스 : 0 ~ n
dp = [0 for _ in range(n+1)]
dp[1] = 0
dp[2] = 1

# 3 ~ n 반복
for i in range(3, n+1):
    dp[i] = ((i-1) * dp[i-1] + (i-1) * dp[i-2]) % mod

print(dp[n])