"""
9328 : 열쇠
50 % 틀림
"""
import sys

t = int(sys.stdin.readline())
ans = ''

while t > 0:
    h, w = map(int, sys.stdin.readline().split())  # ~100
    board = []
    start = []
    door = dict()
    key = ''

    maxCnt = 0
    for i in range(h):
        board.append(list(sys.stdin.readline().strip()))
        for j in range(w):
            if i == 0 or i == h-1 or j == 0 or j == w-1:
                if board[i][j] == '$':
                    board[i][j] = '.'
                    maxCnt += 1
                elif ord('a') <= ord(board[i][j]) <= ord('z'):
                    key += board[i][j]
                    board[i][j] = '.'
            if ord('A') <= ord(board[i][j]) <= ord('Z'):
                if board[i][j] not in door:
                    door[board[i][j]] = []
                door[board[i][j]].append([i, j])

    # 가지고 있는 키
    key += sys.stdin.readline().strip()
    key = key.replace('0', '')
    for c in key:
        cap = c.upper()
        if cap in door:
            dlist = door[cap]
            for d in dlist:
                board[d[0]][d[1]] = '.'

    for c in range(w):
        if board[0][c] == '.':
            start.append([0, c])
        if board[h-1][c] == '.':
            start.append([h-1, c])

    for r in range(h):
        if board[r][0] == '.':
            start.append([r, 0])
        if board[r][w-1] == '.':
            start.append([r, w-1])

    if len(start) == 0 and maxCnt == 0:
        ans += '0\n'
        t -= 1
        continue

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    from collections import deque
    # dq = deque()

    while len(start) > 0:
        st = start.pop()
        dq = deque()

        dq.append(st)
        visit = [[False for _ in range(w)] for _ in range(h)]
        visit[st[0]][st[1]] = True

        while len(dq) > 0:
            posr, posc = dq.popleft()

            for i in range(4):
                nr = posr + dr[i]
                nc = posc + dc[i]
                if 0 <= nr < h and 0 <= nc < w and (not visit[nr][nc]):
                    if board[nr][nc] == '$':
                        board[nr][nc] = '.'
                        visit[nr][nc] = True
                        dq.append([nr, nc])
                        maxCnt += 1
                    elif board[nr][nc] == '.':
                        visit[nr][nc] = True
                        dq.append([nr, nc])
                    elif ord('a') <= ord(board[nr][nc]) <= ord('z'):
                        up = board[nr][nc].upper()
                        if up in door:
                            for d in door[up]:
                                board[d[0]][d[1]] = '.'
                                dq.append(d)
                                visit[d[0]][d[1]] = True

                        board[nr][nc] = '.'
                        visit[nr][nc] = True
                        dq.append([nr, nc])

    ans += (str(maxCnt) + '\n')

    t -= 1

sys.stdout.write(ans)