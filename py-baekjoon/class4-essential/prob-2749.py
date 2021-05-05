"""
2749 : 피보나치 수 3
"""
import sys

n = int(sys.stdin.readline())

mod = 1000000

p = 15 * (mod // 10)

dp = [0 for _ in range(p)]
dp[1] = 1

for i in range(2, p):
    dp[i] = (dp[i-1] + dp[i-2]) % mod

print(dp[n % p])