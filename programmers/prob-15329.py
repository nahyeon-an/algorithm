"""
dp[0][j] = max(dp[0][j-2]+money[j], dp[0][j-1])
dp[0][n] = max(dp[1][n-2] + money[n], dp[0][n-1])
dp[1][k] = max(dp[1][k-2] + money[k], dp[1][k-1])
"""

def solution(money):
    n = len(money)

    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]

    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    dp2[1] = money[1]
    dp2[2] = max(money[1], money[2])

    for i in range(2, n-1):
        dp1[i] = max(dp1[i-2] + money[i], dp1[i-1])
        dp2[i] = max(dp2[i - 2] + money[i], dp2[i - 1])

    dp1[n-1] = max(dp2[n-3] + money[n-1], dp1[n-2])

    return dp1[n-1]

if __name__ == '__main__':
    print(solution([91, 90, 5, 7, 5, 7]))  # 104 ok
    print(solution([90, 0, 0, 95, 1, 1]))  # 185 ok
    print(solution([1, 1, 4, 1, 4]))  # 8 ok
    print(solution([1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]))  # 3000 ok
    print(solution([1000, 1, 0, 1, 2, 1000, 0]))  # 2001 ok
    print(solution([1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000]))  # 2000 ok
    print(solution([11, 0, 2, 5, 100, 100, 85, 1]))  # 198 ok

    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 30
    print(solution([0, 0, 0, 0, 100, 0, 0, 100, 0, 0, 1, 1]))  # 201
    print(solution([1, 2, 3]))  # 3
