# 9465 : 스티커
t = int(input())

for i in range(t):
    n = int(input())
    arr1 = input().split(" ")
    arr2 = input().split(" ")

    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = int(arr1[0])
    dp[1][0] = int(arr2[0])
    dp[0][1] = dp[1][0] + int(arr1[1])
    dp[1][1] = dp[0][0] + int(arr2[1])

    for j in range(n-2):
        # 위
        dp[0][j+2] = max(dp[0][j] + int(arr1[j+2]), dp[1][j] + int(arr1[j+2]))
        dp[0][j+2] = max(dp[0][j+2], dp[1][j+1] + int(arr1[j+2]))
        # 아래
        dp[1][j+2] = max(dp[0][j+1] + int(arr2[j+2]), dp[0][j] + int(arr2[j+2]))
        dp[1][j+2] = max(dp[1][j+2], dp[1][j] + int(arr2[j+2]))

    # print(dp[0])
    # print(dp[1])
    print(max(max(dp[0]), max(dp[1])))

