"""
11505 : 구간 곱 구하기
4% 틀림 -> 아마 update 문제..? (0으로 값을 변화시키는 경우에 대해 잘 처리해줘야 함)
"""
import sys, math

n, m, k = map(int, sys.stdin.readline().split())
div = 1000000007
arr = [int(sys.stdin.readline()) for _ in range(n)]

h = int(math.ceil(math.log2(n)))
num = 1 << (h+1)
t = [0] * num

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start] % div
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(a, tree, 2 * node, start, mid) * \
                 init(a, tree, 2*node+1, mid+1, end)
    tree[node] %= div
    return tree[node]

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    ret = query(tree, 2*node, start, mid, left, right) * \
          query(tree, 2*node+1, mid+1, end, left, right)
    return ret % div

def update(a, tree, node, start, end, idx, org):
    # a[idx]에 해당하는 리프를 찾아야 함
    # 그 노드부터 위로 올라오면서 업데이트
    if idx < start or idx > end:
        return tree[node]
    if start == end:
        if tree[node] == org:
            tree[node] = a[idx] % div
        return tree[node]
    mid = (start + end) // 2
    tree[node] = update(a, tree, 2*node, start, mid, idx, org) * \
                 update(a, tree, 2*node+1, mid+1, end, idx, org)
    tree[node] %= div
    return tree[node]


init(arr, t, 1, 0, n-1)
print()
print(t)

ans = ''
for _ in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        org = arr[b-1]
        arr[b-1] = c
        update(arr, t, 1, 0, n-1, b-1, org)
        print(t)
    else:
        ans += str(query(t, 1, 0, n-1, b-1, c-1))
        ans += '\n'

sys.stdout.write(ans)