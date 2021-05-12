"""
17490 : 일감호에 다리 놓기
17 % 자꾸 틀리네...? -> 아마 recursion depth 때문에 전체를 순회하지 못해서 에러였을 것 같다
유니온 파인드는 메모리 초과라서 안 됨
"""
import sys
sys.setrecursionlimit(10 ** 9)

n, m, k = map(int, sys.stdin.readline().split())
snum = list(map(int, sys.stdin.readline().split()))

nedges = [(i + 1) % n for i in range(n + 1)]
nedges[0] = -1

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    # nedges[u] = -1
    if u < v:
        if u == 1 and v == n:
            nedges[n] = -1
        else:
            nedges[u] = -1
    else:
        if u == n and v == 1:
            nedges[n] = -1
        else:
            nedges[v] = -1


if m <= 1:
    sys.stdout.write("YES\n")
    sys.exit(0)

def union(par, x, y):
    px = find(par, x)
    py = find(par, y)
    if px == py:
        return
    if px < py:
        par[py] = px
    else:
        par[px] = py

def find(par, x):
    if par[x] == x:
        return x
    par[x] = find(par, par[x])
    return par[x]


par = [i for i in range(n + 1)]
for i in range(1, n + 1):
    if nedges[i] != -1:
        union(par, i, nedges[i])

hq = [[e, i+1] for i, e in enumerate(snum)]

import heapq
heapq.heapify(hq)

cnt = 0
for i in range(n):
    cur = heapq.heappop(hq)
    if find(par, 0) != find(par, cur[1]):
        cnt += cur[0]
        union(par, 0, cur[1])

if cnt > k:
    sys.stdout.write("NO\n")
else:
    sys.stdout.write("YES\n")


# 모두 한 집합인지 확인
# flag = True
# for i in range(1, n+1):
#     if par[i] != 0 and find(par, 0) != find(par, i):
#         flag = False
#         break
#
# if flag:
#     sys.stdout.write("YES\n")
# else:
#     sys.stdout.write("NO\n")

