"""
17398 : 통신망 분할
pypy : 8 % 메모리 초과.. 깊이를 줄이면 틀림...
python : 8 % 시간 초과
rank 최적화 하기
"""
import sys
sys.setrecursionlimit(10 ** 6)
# n : 통신탑의 개수 10 ^ 5
# m : 통신탑 사이의 연결 개수 10 ^ 5
# q : 분할 횟수
n, m, q = map(int, sys.stdin.readline().split())

def union(par, x, y):
    px = find(par, x)
    py = find(par, y)
    if px == py:
        return
    if rank[px] < rank[py]:
        # y에 합침
        par[px] = py
    else:
        # x에 합침
        par[py] = px

        if rank[px] == rank[py]:
            rank[px] += 1

def find(par, x):
    if par[x] == x:
        return x
    par[x] = find(par, par[x])
    return par[x]


par = [i for i in range(n+1)]
rank = [0] * (n+1)
link = [[-1, -1]]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    link.append([x, y])
    # union(par, x, y)

cut = [int(sys.stdin.readline()) for _ in range(q)]

for i in range(1, m):
    if i in cut:
        continue
    union(par, link[i][0], link[i][1])
# print(par)
print(rank)

ans = 0
for c in cut[::-1]:
    p1 = find(par, link[c][0])
    p2 = find(par, link[c][1])
    if p1 != p2:
        # link[c][0]의 집합의 개수
        cnt1 = 0
        cnt2 = 0
        for p in par:
            if p == p1:
                cnt1 += 1
            if p == p2:
                cnt2 += 1
        ans += cnt1 * cnt2
        union(par, link[c][0], link[c][1])

print(ans)
print(par)
