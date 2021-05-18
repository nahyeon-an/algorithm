"""
10942 : 팰린드롬
Pypy는 시간초과
Python은 통과..
"""
import sys

# ~ 2000
n = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())  # ~ 10^6

dp = [[False for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n):
    dp[i][i] = True
    if num[i] == num[i+1]:
        dp[i][i+1] = True
    else:
        dp[i][i+1] = False
dp[n][n] = True

for length in range(2, n+1):
    for i in range(1, n+1-length):
        dp[i][i+length] = dp[i+1][i+length-1] and (num[i] == num[i+length])

ans = ''
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    if dp[s][e]:
        ans += '1\n'
    else:
        ans += '0\n'

sys.stdout.write(ans)