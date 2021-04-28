import sys

a, b = sys.stdin.readline().split(" ")
a, b = int(a), int(b)

dp = [[0 for _ in range(b+1)] for _ in range(a+1)]

for i in range(a+1):
    dp[i][0] = 1

for i in range(b+1):
    dp[0][i] = 1

for i in range(min(a+1, b+1)):
    dp[i][i] = 1

for i in range(1, a+1):
    for j in range(1, b+1):
        if i == 1 and j == 1:
            continue

        if dp[i][j] != 0:
            continue

        # a 주머니에서 가져가는 경우
        for k in range(i):
            dp[i][j] = max(dp[k][j], dp[i][j])
        # b 주머니에서 가져가는 경우
        for k in range(j):
            dp[i][j] = max(dp[i][j], dp[i][k])
        # a, b, 모두에서 똑같이 가져가는 경우
        for k in range(min(i, j)):
            dp[i][j] = max(dp[i][j], dp[i-k-1][j-k-1])

        dp[i][j] += 1

if dp[a][b] % 2 == 1:
    print(0, dp[a][b])  # A 승리
else:
    print(1, dp[a][b])  # B 승리
