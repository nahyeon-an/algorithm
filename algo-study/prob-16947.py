"""
16947 : 서울 지하철 2호선
"""
import sys

sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())
adjList = {i: [] for i in range(1, n+1)}
for i in range(n):
    u, v = map(int, sys.stdin.readline().split())
    adjList[u].append(v)
    adjList[v].append(u)

# 1. cycle 찾기, 속하는 점도 찾기
# 2. cycle 에 속하는 점에서 연결된 점들로 dfs 해서 dist 구하기

visit = [False for _ in range(n+1)]

cycle = set()
def is_cycle(st, prev, here, p):
    visit[here] = True
    p.append(here)

    for nex in adjList[here]:
        if prev != st and st == nex:
            for i in p:
                cycle.add(i)
            return
        if not visit[nex]:
            visit[nex] = True
            is_cycle(st, here, nex, p.copy())

for i in range(1, n+1):
    is_cycle(i, 0, i, [])
    if len(cycle) > 2:
        # print(i)
        break
    else:
        cycle = set()
        visit = [False for _ in range(n + 1)]

# print(cycle)

dist = [-1 for _ in range(n+1)]
def dfs(here, cnt):
    dist[here] = cnt

    for nex in adjList[here]:
        if dist[nex] == -1:
            dist[nex] = dist[here] + 1
            dfs(nex, dist[here] + 1)

for c in cycle:
    dist[c] = 0

for c in cycle:
    dfs(c, 0)

print(" ".join(map(str, dist[1:])))