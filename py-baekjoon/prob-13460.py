"""
13460 : 구슬 탈출 2
"""
import sys

n, m = map(int, sys.stdin.readline().split())

board = []
start = []
for i in range(n):
    temp = sys.stdin.readline()
    line = []
    for j in range(m):
        line += temp[j]
        if temp[j] == 'R':
            start = [i, j]
    board.append(line)

# 빨간 구슬이 구멍에 가도록 (파란 구슬은 들어가면 안 됨)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

visit = [[False for _ in range(m)] for _ in range(n)]

def bfs(r, c):
    if board[r][c] == 'O':
        print('{}, {}'.format(r, c))
        return

    from collections import deque

    dq = deque()
    dq.append([r, c])

    visit[r][c] = True

    ret = 0

    while dq:
        posr, posc = dq.popleft()
        print(posr, posc)

        for i in range(4):
            # 빨간 구슬 기울이기
            nr1, nc1 = posr + dr[i], posc + dc[i]
            while board[nr1][nc1] != '#' and board[nr1][nc1] != 'B':
                if board[nr1][nc1] == 'O':
                    bfs(nr1, nc1)
                nr1 += dr[i]
                nc1 += dc[i]

            if not visit[nr1-dr[i]][nc1-dc[i]]:
                bfs(nr1-dr[i], nc1-dc[i])
                # dq.append([nr1-dr[i], nc1-dc[i]])
                # visit[nr1-dr[i]][nc1-dc[i]] = True

            # 파란 구슬 기울이기
            nr2, nc2 = posr + dr[i], posc + dc[i]
            while board[nr2][nc2] != '#' and board[nr2][nc2] != 'R':
                nr2 += dr[i]
                nc2 += dc[i]

            # print(nr2 - dr[i], nc2 - dc[i])


bfs(*start)
