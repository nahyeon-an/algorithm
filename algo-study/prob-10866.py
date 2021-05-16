"""
10866 : 최솟값
"""
import sys, math

inf = 1000000001
def initMin(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    else:
        tree[node] = min(initMin(a, tree, node * 2, start, (start+end) // 2),
                     initMin(a, tree, node * 2 + 1, (start+end)//2 + 1, end))
        return tree[node]

def queryMin(tree, node, start, end, left, right):
    if left > end or right < start:
        return inf
    if left <= start and end <= right:
        return tree[node]
    q1 = queryMin(tree, node * 2, start, (start+end)//2, left, right)
    q2 = queryMin(tree, node * 2 + 1, (start+end)//2+1, end, left, right)
    return min(q1, q2)

n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
h = int(math.ceil(math.log2(n)))
num = 1 << (h+1)
t = [0] * num

initMin(arr, t, 1, 0, n-1)

ans = ""
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    ans += (str(queryMin(t, 1, 0, n-1, a-1, b-1)) + "\n")
sys.stdout.write(ans)