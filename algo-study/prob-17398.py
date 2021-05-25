"""
17398 : 통신망 분할
union-find에서 어떤 노드가 속한 집합의 노드의 개수를 빨리 찾는 방법
"""
import sys

n, m, q = map(int, sys.stdin.readline().split())

connect = [i for i in range(n+1)]

# cost[i] : 노드 i의 집합에 속하는 노드의 개수
cost = [1 for _ in range(n+1)]

def find(x):
    if connect[x] == x:
        return x
    connect[x] = find(connect[x])
    return connect[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px == py:
        return

    connect[px] = py
    cost[py] += cost[px]

link = [[-1, -1]]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    link.append([x, y])

cut = [int(sys.stdin.readline()) for _ in range(q)]

print(connect, cost)

for i in range(1, m+1):
    if i not in cut:
        union(link[i][0], link[i][1])

ans = 0
for i in range(q-1, -1, -1):
    j = cut[i]
    p1 = find(link[j][0])
    p2 = find(link[j][1])
    if p1 != p2:
        ans += (cost[p1] * cost[p2])
        union(p1, p2)
        print(connect, cost)

# print(connect, cost)
print(ans)
# print(par)
