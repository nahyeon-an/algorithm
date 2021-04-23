"""
17404 : RGB 거리 2
"""
import sys

n = int(sys.stdin.readline())
cost = dict()
# dp[i][j] : i번 집을 j 색으로 칠할 때의 비용
inf = 1000000
dp = [[inf for _ in range(3)] for _ in range(n+1)]

for i in range(1, n+1):
    cost[i] = list(map(int, sys.stdin.readline().split(" ")))

# 1번 집을 빨간색으로 칠함
dp[1][0] = cost[1][0]
for i in range(2, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
# dp[n][1], dp[n][2] 만 존재 가능
dp[n][1] = min(dp[n-1][0], dp[n-1][2]) + cost[n][1]
dp[n][2] = min(dp[n-1][0], dp[n-1][1]) + cost[n][2]

mini = min(dp[n][1], dp[n][2])

# 1번 집을 초록색으로 칠함
dp = [[inf for _ in range(3)] for _ in range(n+1)]
dp[1][1] = cost[1][1]
for i in range(2, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
# dp[n][0], dp[n][2] 만 존재 가능
dp[n][0] = min(dp[n-1][1], dp[n-1][2]) + cost[n][0]
dp[n][2] = min(dp[n-1][0], dp[n-1][1]) + cost[n][2]

mini = min(mini, dp[n][0])
mini = min(mini, dp[n][2])

# 1번 집을 파란색으로 칠함
dp = [[inf for _ in range(3)] for _ in range(n+1)]
dp[1][2] = cost[1][2]
for i in range(2, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
dp[n][0] = min(dp[n-1][1], dp[n-1][2]) + cost[n][0]
dp[n][1] = min(dp[n-1][0], dp[n-1][2]) + cost[n][1]

mini = min(mini, dp[n][0])
mini = min(mini, dp[n][1])

print(mini)

# 세 단계를 모두 합칠 수 없음 - 왜냐면 합치는 순간 최종 비용에 반영되기 때문