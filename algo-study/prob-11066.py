"""
11066 : 파일 합치기
"""
import sys
sys.setrecursionlimit(10 ** 4)

t = int(sys.stdin.readline())

while t > 0:
    k = int(sys.stdin.readline())  # <= 500, 소설을 구성하는 장의 수
    size = [0] + list(map(int, sys.stdin.readline().split()))
    tot = [0] * (k+1)
    for i in range(1, k+1):
        tot[i] = tot[i-1] + size[i]

    # dp[i][j] := 배열의 i~j를 합치는 데에 드는 최소 비용
    dp = [[-1] * (k+1) for _ in range(k+1)]

    inf = 50000005

    def solve(start, end):
        """
        size의 start ~ end 를 합침
        """
        if dp[start][end] != -1:
            return dp[start][end]

        if start == end:
            dp[start][end] = 0
            return dp[start][end]

        if start + 1 == end:
            dp[start][end] = size[start] + size[end]
            return dp[start][end]

        dp[start][end] = inf
        for i in range(start, end):
            s1 = solve(start, i)
            s2 = solve(i + 1, end)
            dp[start][end] = min(dp[start][end], s1+s2)

        dp[start][end] += (tot[end] - tot[start - 1])
        return dp[start][end]

    print(solve(1, k))

    t -= 1