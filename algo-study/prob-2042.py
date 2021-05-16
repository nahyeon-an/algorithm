"""
2042 : 구간 합 구하기 (세그먼트 트리)
"""
import sys, math

n, m, k = map(int, sys.stdin.readline().split())

# m : 수를 업데이트 하는 횟수
# k : 조회 횟수

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(a, tree, node * 2, start, mid) + \
                 init(a, tree, node * 2 + 1, mid + 1, end)
    return tree[node]

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    ret = query(tree, 2 * node, start, mid, left, right) + \
          query(tree, 2*node + 1, mid +1, end, left, right)
    return ret

def update(tree, node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] = tree[node] + diff
    if start != end:
        mid = (start + end) // 2
        update(tree, node * 2, start, mid, idx, diff)
        update(tree, node * 2 + 1, mid + 1, end, idx, diff)


arr = [int(sys.stdin.readline()) for _ in range(n)]
h = int(math.ceil(math.log2(n)))
num = 1 << (h+1)
t = [0] * num

init(arr, t, 1, 0, n-1)

ans = ""
for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        d = c - arr[b-1]
        arr[b-1] = c
        update(t, 1, 0, n-1, b-1, d)
    else:
        ans += str(query(t, 1, 0, n-1, b-1, c-1))
        ans += "\n"
sys.stdout.write(ans)