"""
10711 : 모래성
11 % 시간 초과
"""
import sys

h, w = map(int, sys.stdin.readline().split())

board = [[0] * w for _ in range(h)]
visit = [[False] * w for _ in range(h)]

from collections import deque

dq = deque()
for i in range(h):
    temp = sys.stdin.readline().strip()
    for j in range(w):
        if temp[j] != '.':
            board[i][j] = int(temp[j])
        else:
            dq.append([i, j])
            visit[i][j] = True

dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, 1, -1, 1, -1, 1, -1]

ans = 0
length = len(dq)
while dq:
    ans += 1
    while length > 0:
        cur = dq.popleft()
        # print(visit[cur[0]][cur[1]], cur)

        for i in range(8):
            nr, nc = cur[0] + dr[i], cur[1] + dc[i]
            if 0 <= nr < h and 0 <= nc < w and not visit[nr][nc]:
                if board[nr][nc] > 0:
                    board[nr][nc] -= 1
                if board[nr][nc] == 0:
                    dq.append([nr, nc])
                    visit[nr][nc] = True
        length -= 1
    length = len(dq)
    # print(board)

print(ans-1)