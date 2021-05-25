"""
9328 : 열쇠
"""
import sys

t = int(sys.stdin.readline())

# ans = ''
while t > 0:
    h, w = map(int, sys.stdin.readline().split())

    board = [['.'] * (w+2)]
    door = {chr(i): [] for i in range(ord('A'), ord('Z')+1)}

    for i in range(h):
        temp = sys.stdin.readline()
        line = ['.']
        for j in range(len(temp)):
            line += temp[j]

            if ord('A') <= ord(line[j]) <= ord('Z'):
                door[line[j]].append([i+1, j])

        line += ['.']
        board.append(line)
    board.append(['.'] * (w+2))

    h += 2
    w += 2

    key = sys.stdin.readline().strip()
    key = key.replace('0', '')

    # 처음부터 가지고 있는 열쇠에 해당하는 문을 다 없애줌
    for c in key:
        doors = door[c.upper()]
        for d in doors:
            board[d[0]][d[1]] = '.'
        door[c.upper()] = []

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    def bfs(r, c):
        from collections import deque

        dq = deque()
        dq.append([r, c])

        visit = [[False for _ in range(w)] for _ in range(h)]
        visit[r][c] = True

        ret = 0

        while dq:
            posr, posc = dq.popleft()

            for i in range(4):
                nr = posr + dr[i]
                nc = posc + dc[i]

                if 0 <= nr < h and 0 <= nc < w and board[nr][nc] != '*':
                    if not visit[nr][nc]:
                        if ord('A') <= ord(board[nr][nc]) <= ord('Z'):
                            continue
                        elif board[nr][nc] == '$':
                            ret += 1
                            board[nr][nc] = '.'
                        elif ord('a') <= ord(board[nr][nc]) <= ord('z'):
                            # 키 값
                            doors = door[board[nr][nc].upper()]
                            for d in doors:
                                board[d[0]][d[1]] = '.'
                            # visit 초기화
                            if doors:
                                door[board[nr][nc].upper()] = []
                                visit = [[False for _ in range(w)] for _ in range(h)]
                        dq.append([nr, nc])
                        visit[nr][nc] = True
        return ret

    print(bfs(0, 0))
    # ans += str(bfs(0, 0))
    # ans += '\n'

    t -= 1

# print(ans)