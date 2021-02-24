# 2206 : 벽 부수고 이동하기
from collections import deque

n, m = input().split(" ")
n = int(n)
m = int(m)

map = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(m):
        map[i][j] = int(line[j])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]

    q = deque()
    q.append([r, c, 1])
    visit[1][r][c] = 1

    while len(q) != 0:
        v = q.popleft()

        if v[0] == n-1 and v[1] == m-1:
            return visit[v[2]][v[0]][v[1]]

        for i in range(4):
            nr = v[0] + dr[i]
            nc = v[1] + dc[i]
            if nr < 0 or nr >= n:
                continue
            if nc < 0 or nc >= m:
                continue
            if map[nr][nc] == 0:
                if visit[v[2]][nr][nc] != 0:
                    continue
                q.append([nr, nc, v[2]])
                visit[v[2]][nr][nc] = visit[v[2]][v[0]][v[1]] + 1
            else:
                if v[2] <= 0:
                    continue
                q.append([nr, nc, v[2] - 1])
                visit[v[2]-1][nr][nc] = visit[v[2]][v[0]][v[1]] + 1
    return -1

print(bfs(0,0))
