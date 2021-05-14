"""
9328 : 열쇠

https://jaimemin.tistory.com/692
"""
import sys

t = int(sys.stdin.readline())
ans = ''

while t > 0:
    h, w = map(int, sys.stdin.readline().split())
    board = []
    door = dict()
    cnt = 0
    key = ''

    board.append(['.'] * (w + 2))
    for i in range(h):
        board.append(['.'] + list(sys.stdin.readline().strip()) + ['.'])

        for j in range(w):
            if ord('A') <= ord(board[i][j]) <= ord('Z'):
                if board[i][j] not in door:
                    door[board[i][j]] = []
                door[board[i][j]].append([i, j])
    board.append(['.'] * (w + 2))

    key += sys.stdin.readline().strip()
    key = key.replace('0', '')

    for k in key:
        if k.upper() not in door:
            continue
        for d in door[k.upper()]:
            board[d[0]][d[1]] = '.'

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    from collections import deque

    v = [[False for _ in range(w+2)] for _ in range(h+2)]
    dq = deque()
    dq.append([0,0])
    v[0][0] = True

    while len(dq) > 0:
        posr, posc = dq.popleft()

        for i in range(4):
            nr = posr + dr[i]
            nc = posc + dc[i]

            if 0 <= nr < h+2 and 0 <= nc < w+2 and not v[nr][nc]:
                if board[nr][nc] == '$':
                    cnt += 1
                    board[nr][nc] = '.'
                    dq.append([nr, nc])
                    v[nr][nc] = True
                elif board[nr][nc] == '.':
                    dq.append([nr, nc])
                    v[nr][nc] = True
                elif ord('a') <= ord(board[nr][nc]) <= ord('z'):
                    k = board[nr][nc].upper()
                    if k not in door:
                        board[nr][nc] = '.'
                        v.append([nr, nc])
                        v[nr][nc] = True
                        continue
                    for d in door[k]:
                        board[d[0]][d[1]] = '.'

                    board[nr][nc] = '.'
                    v = [[False for _ in range(w+2)] for _ in range(h+2)]
                    dq.clear()
                    dq.append([nr, nc])
                    v[nr][nc] = True

    print(cnt)
    ans += str(cnt)
    t -= 1

sys.stdout.write(ans)