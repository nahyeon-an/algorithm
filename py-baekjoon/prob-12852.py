# 12852 : 1로 만들기 2
n = int(input()) # 1 ~ 1000000

dp = [[0 for _ in range(1000005)] for _ in range(3)]
ret = []

for i in range(n, 0, -1):
    if i % 3 == 0:
        dp[0][i] += 1
    if i % 2 == 0:
        dp[1][i] += 1
    dp[2][i] += 1