"""
2662 : 기업투자
"""
import sys

# ~300, ~20
n, m = map(int, sys.stdin.readline().split())

profit = [[] for _ in range(n+1)]

# dp[i][j] : 금액 i를 회사 j 까지(j+1개)에 투자할 때 최대 이익
# 금액 : 0 ~ n
# 회사 : 0 ~ m-1
dp = [[0] * m for _ in range(n+1)]
invest = [[0] * m for _ in range(n+1)]
# 최대 이익을 얻었을 때 기업별 투자 금액

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    profit[temp[0]] += temp[1:]

profit[0] = [0] * m

print(profit) # 행 인덱스 = 금액, 열 인덱스 = 회사 번호

# 1개의 기업 ~ m개의 기업
for i in range(n+1):
    dp[i][0] = profit[i][0]
    invest[i][0] = i

# 최대 이익 = dp[n][m-1]
for j in range(1, m):
    for i in range(1, n + 1):
        for k in range(i+1):
            if dp[i][j] < dp[k][j-1] + profit[i-k][j]:
                dp[i][j] = dp[k][j - 1] + profit[i - k][j]
                invest[i][j] = i-k

print(dp[n][m-1])  # 기업 m-1에 투자 금액 = invest[n][m-1]
print(dp)

ans = []
val = n
for i in range(m-1, -1, -1):
    ans.append(invest[val][i])
    # print(invest[val][i])
    val = val - invest[val][i]

print(invest)

print(" ".join(map(str, ans[::-1])))
# print(" ".join(map(str, invest)))
