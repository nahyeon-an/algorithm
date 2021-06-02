import sys

n, k = map(int, sys.stdin.readline().split())

dp = [[0] * k for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = 1

for i in range(1, k):
    dp[i][i] = 1

# dp[i][j] : 1 ~ i일에서 j번 결근하는 경우의 수
