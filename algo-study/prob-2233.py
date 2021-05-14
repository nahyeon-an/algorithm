"""
2233 : 사과나무
"""
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
x, y = map(int, sys.stdin.readline().split())

depth = [-1 for _ in range(n)]
par = [-1 for _ in range(n)]  # 부모 노드 정보 ?
arr = [-1 for _ in range(2*n)]

cnt = 0
node = 0
st = [-1]
# depth
for i in range(2 * n):
    if s[i] == '0':
        st.append(node)
        arr[i] = node
        cnt += 1
        node += 1
    else:
        cur = st.pop()
        depth[cur] = cnt
        par[cur] = st[-1]
        arr[i] = cur
        cnt -= 1

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = par[a]
        else:
            b = par[b]
    while a != b:
        a = par[a]
        b = par[b]
    return a

rm = lca(arr[x-1], arr[y-1])
answer = ''
for i in range(2*n):
    if arr[i] == rm:
        answer += (str(i+1) + " ")

print(answer)
