"""
2233 : 사과나무
"""
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
x, y = map(int, sys.stdin.readline().split())

# 1. s -> tree 모양 찾기..
# 일단 트리를 어떻게 저장해야할지 모르겠다...
# 구현이 전혀 안 되네.....ㅋㅋ
tree = [[0 for _ in range(n)] for _ in range(n)]
depth = [-1 for _ in range(n)]
parent = []  # 부모 노드 정보 ?

node = 0
par = -1
for i in range(2*n):
    print(par, node)
    if s[i] == '0':
        if par != -1:
            tree[par][node] = 1
            tree[node][par] = 1
        par = node
        node += 1


cnt = 0
node = 0
for i in range(2 * n):
    if s[i] == '0':
        cnt += 1
        depth[node] = cnt
        node += 1
    else:
        cnt -= 1

# 노드 0 ~ n-1 의 레벨
print(depth)

# 2. x와 y의 최소 공통 조상을 삭제하는 문제 같다

# 제거해야 할 사과를 나타내는 정수 리턴