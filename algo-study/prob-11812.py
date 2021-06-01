"""
11812 : K진 트리
"""
import sys

# n : 전체 노드의 개수
# k : k 진트리, 자식노드 최대 개수
# q : 질의 개수
n, k, q = map(int, sys.stdin.readline().split())

if k == 1:
    for _ in range(q):
        x, y = map(int, sys.stdin.readline().split())
        print(abs(x - y))
    sys.exit(0)

# 핵심 : k진 트리에서 (루트노드가 1일 떄)
# 노드 node 번의 부모노드 번호 = (node - 2) // k + 1
def lca(a, b):
    pa = (a - 2) // k + 1
    pb = (b - 2) // k + 1

    ret = 0
    while a != b:
        if a > b:
            a = pa
            pa = (a - 2) // k + 1
            ret += 1
        else:
            b = pb
            pb = (b - 2) // k + 1
            ret += 1

    return ret

for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    print(lca(x, y))