"""
2186 : 문자판
dp로 풀기 -> 83 %
"""
import sys

n, m, k = map(int, sys.stdin.readline().split())

board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

word = list(sys.stdin.readline().strip())

dp = [[[-1 for _ in range(len(word))] for _ in range(m)] for _ in range(n)]

def solve(r, c, idx):
    # board[r][c]에서 k로 움직여서 word[idx]를 찾는다
    if idx == len(word):
        return 1

    if dp[r][c][idx] != -1:
        return dp[r][c][idx]

    # ret = 0
    dp[r][c][idx] = 0
    for dk in range(1, k+1):
        if 0 <= r-dk < n and word[idx] == board[r-dk][c]:
            dp[r][c][idx] += solve(r-dk, c, idx+1)
            # ret += solve(r-dk, c, idx+1)
        if 0 <= r+dk < n and word[idx] == board[r+dk][c]:
            dp[r][c][idx] += solve(r+dk, c, idx+1)
            # ret += solve(r+dk, c, idx+1)
        if 0 <= c-dk < m and word[idx] == board[r][c-dk]:
            dp[r][c][idx] += solve(r, c-dk, idx+1)
            # ret += solve(r, c-dk, idx+1)
        if 0 <= c+dk < m and word[idx] == board[r][c+dk]:
            dp[r][c][idx] += solve(r, c+dk, idx+1)
            # ret += solve(r, c+dk, idx+1)

    # dp[r][c][idx] = ret
    # return ret
    print(dp[r][c][idx])
    return dp[r][c][idx]


ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == word[0]:
            ans += solve(i, j, 1)
print(ans)