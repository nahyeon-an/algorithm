"""
11567 : 겨울왕국
"""
import sys

# 행 개수, 열 개수
n, m = map(int, sys.stdin.readline().split())

board = [['X'] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    temp = sys.stdin.readline().strip()
    for j in range(1, m+1):
        if temp[j-1] == '.':
            board[i][j] = temp[j-1]

r1, c1 = map(int, sys.stdin.readline().split())
r2, c2 = map(int, sys.stdin.readline().split())

# . : 손상 X
# X : 손상 O
# 손상되지 않은 얼음 칸으로 이동
# 다른 칸으로 이동하면 그 칸은 손상 상태 -> 다시 방문 불가
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

from collections import deque

def bfs(r, c):
    dq = deque()
    dq.append([r, c])

    while dq:
        posr, posc = dq.popleft()

        for i in range(4):
            nr = posr + dr[i]
            nc = posc + dc[i]

            if 0 < nr <= n and 0 < nc <= m:
                if nr == r2 and nc == c2 and board[nr][nc] == 'X':
                    return True
                if board[nr][nc] == '.':
                    dq.append([nr, nc])
                    board[nr][nc] = 'X'
    return False

# 탈출 가능 ? 불가능 ?
if bfs(r1, c1):
    print("YES")
else:
    print("NO")