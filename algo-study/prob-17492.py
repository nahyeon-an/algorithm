"""
17492 : 바둑알 점프
60점... 51%
뭔가 틀리는 경우가 있는 것 같다.
"""
from copy import deepcopy
import sys

sys.setrecursionlimit(10**4)

n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

start = []
num = 0
for i in range(n):
    for j in range(n):
        if m[i][j] == 2:
            start.append([i, j])
            num += 1

# 0 : 빈칸
# 1 : 벽
# 2 : 바둑알
dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, 1, -1, 1, -1, 1, -1]

def solve(r, c, board, cnt):
    """
    r, c에서 움직일 곳을 찾아서 이동
    num 개의 바둑알이 존재
    """
    if cnt == 1:
        return cnt

    ret = 10
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 2:
            if 0 <= nr+dr[i] < n and 0 <= nc+dc[i] < n \
                    and board[nr+dr[i]][nc+dc[i]] == 0:
                board[nr + dr[i]][nc + dc[i]] = 2
                board[nr][nc] = 0
                board[r][c] = 0
                ret = min(ret, solve(nr + dr[i], nc + dc[i], deepcopy(board), cnt - 1))
                board[nr + dr[i]][nc + dc[i]] = 0
                board[nr][nc] = 2
                board[r][c] = 2
    return ret


for st in start:
    ret = solve(st[0], st[1], deepcopy(m), num)
    if ret == 1:
        sys.stdout.write("Possible\n")
        sys.exit(0)

sys.stdout.write("Impossible\n")

