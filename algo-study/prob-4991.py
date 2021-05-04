"""
4991 : 로봇 청소기
"""
from collections import deque
import sys

temp = []

while True:
    w, h = sys.stdin.readline().strip().split(" ")
    w, h = int(w), int(h)

    if w == 0 and h == 0:
        break

    board = []
    start = []
    trash = []

    dirty = 0
    for i in range(h):
        board.append(list(sys.stdin.readline().strip()))
        for j in range(w):
            if board[i][j] == 'o':
                start = [i, j]
            if board[i][j] == '*':
                trash.append([i, j])

    dist = [[-1 for _ in range(len(trash)+1)] for _ in range(len(trash)+1)]
    for i in range(len(trash)+1):
        dist[i][i] = 0

    def bfs(r, c, i, tr, tc, ti):
        dq = deque()
        visit = [[-1 for _ in range(w)] for _ in range(h)]
        if visit[r][c] == -1:
            dq.append([r, c])
            visit[r][c] = 0

        while len(dq) > 0:
            cur = dq.popleft()
            posr, posc = cur[0], cur[1]

            if board[posr][posc] == '*':
                if tr == posr and tc == posc:
                    dist[i][ti] = visit[posr][posc]
                    dist[ti][i] = visit[posr][posc]

            if posr+1 < h and visit[posr+1][posc] == -1 \
                    and board[posr+1][posc] != 'x':
                dq.append([posr+1, posc])
                visit[posr+1][posc] = visit[posr][posc] + 1

            if 0 <= posr-1 and visit[posr-1][posc] == -1 \
                    and board[posr-1][posc] != 'x':
                dq.append([posr-1, posc])
                visit[posr-1][posc] = visit[posr][posc] + 1

            if posc+1 < w and visit[posr][posc+1] == -1 \
                    and board[posr][posc+1] != 'x':
                dq.append([posr, posc+1])
                visit[posr][posc+1] = visit[posr][posc] + 1

            if 0 <= posc-1 and visit[posr][posc-1] == -1 \
                    and board[posr][posc-1] != 'x':
                dq.append([posr, posc-1])
                visit[posr][posc-1] = visit[posr][posc] + 1

    for idx, t in enumerate(trash):
        bfs(start[0], start[1], 0, t[0], t[1], idx+1)

    for i in range(len(trash)):
        for j in range(i+1, len(trash)):
            bfs(trash[i][0], trash[i][1], i+1, trash[j][0], trash[j][1], j+1)

    # 2. dist 배열에서 외판원 문제로 방문 순서 찾기
    # 다만 시작점으로 돌아오는 비용은 제외함
    n = 1 + len(trash)

    cnt = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if dist[i][j] == -1:
                cnt += 1
        if cnt == n-1:
            break
        else:
            cnt = 0

    if cnt != 0:
        temp.append(str(-1))
        continue

    dp = [[None for _ in range(1 << n)] for _ in range(n)]

    def solve(here, visited):
        if visited == (1 << n) - 1:
            # 모두 방문한 경우 (1111)
            return 0

        if dp[here][visited] != None:
            return dp[here][visited]

        ret = 405
        for i in range(n):
            nex = (1 << i) | visited
            if dist[here][i] == 0:
                continue
            if (visited & (1 << i)) != 0:
                # 방문한 경우
                continue
            ret = min(ret, solve(i, nex) + dist[here][i])

        dp[here][visited] = ret
        return ret

    ans = solve(0, 1)
    if ans < 0:
        temp.append(str(-1))
    else:
        temp.append(str(ans))

sys.stdout.write("\n".join(temp))