"""
2482 : 색상환
"""
import sys

n = int(sys.stdin.readline())  # 4 ~ 1000
k = int(sys.stdin.readline())  # 1 ~ n

mod = 1000000003

if k >= (n // 2 + 1):
    # 불가능한 경우
    print(0)

# dp[i][j][k] = 색상 i ~ j 중에서 k개를 뽑는 경우의 수 -> 메모리 초과
dp = [[[0 for _ in range(k+1)] for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i][1] = 1

for i in range(1, n):
    for j in range(i+1, n+1):
        for pick in range(1, k+1):
            if pick == 1:
                dp[i][j][pick] = dp[i][j-1][pick] + 1
            else:
                dp[i][j][pick] = dp[i][j-2][pick-1] + dp[i][j-1][pick]

# n번째 루프
dp[1][n][1] = dp[1][n-1][1] + 1
for pick in range(2, k+1):
    dp[1][n][pick] = dp[1][n-1][pick] + (dp[2][n-2][pick-1])

print(dp[1][n][k] % mod)