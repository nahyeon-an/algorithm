"""
2146 : 다리 만들기
Pypy로는 메모리에러 Python3로는 통과..
알수없는 파이썬..
"""
import sys
sys.setrecursionlimit(10**7)

# 100 이하
n = int(sys.stdin.readline())

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

# 섬의 번호
num = [[ 0 for _ in range(n) ] for _ in range(n)]
visit = [[ False for _ in range(n) ] for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c, cnt):
    visit[r][c] = True
    num[r][c] = cnt

    for i in range(4):
        posr = r + dr[i]
        posc = c + dc[i]
        if 0 <= posr < n and 0 <= posc < n:
            if not visit[posr][posc] and board[posr][posc] == 1:
                dfs(posr, posc, cnt)

c = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visit[i][j]:
            dfs(i, j, c)  # 섬의 번호 1 ~
            c += 1

# 존재하는 섬의 개수 = c - 1
# bfs
from collections import deque
def bfs(cnt):
    # cnt 번 섬에서 다른 섬으로의 거리
    dq = deque()
    v = [[-1 for _ in range(n)] for _ in range(n)]

    # cnt섬의 좌표
    for i in range(n):
        for j in range(n):
            if num[i][j] == cnt:
                dq.append([i, j])
                v[i][j] = 0

    while len(dq) > 0:
        cur = dq.popleft()

        # 4방확인
        for i in range(4):
            posr = cur[0] + dr[i]
            posc = cur[1] + dc[i]

            if 0 <= posr < n and 0 <= posc < n:
                if board[posr][posc] == 0 and v[posr][posc] == -1:
                    dq.append([posr, posc])
                    v[posr][posc] = v[cur[0]][cur[1]] + 1
                if board[posr][posc] == 1 and num[posr][posc] != cnt:
                    return v[cur[0]][cur[1]]

ans = 100000
for i in range(1, c):
    ret = bfs(i)
    if ret < ans:
        ans = ret

sys.stdout.write(str(ans) + "\n")