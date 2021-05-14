"""
2357 : 최솟값과 최댓값
pypy => 시간초과
python => 통과
"""
import sys, math

n, m = map(int, sys.stdin.readline().split())

arr = [int(sys.stdin.readline()) for _ in range(n)]
h = int(math.ceil(math.log2(n)))
num = 1 << (h+1)
# t = [0] * num

max_tree = [0] * num
min_tree = [0] * num

inf = 1000000001

def initMin(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = min(initMin(a, tree, node * 2, start, mid),
                         initMin(a, tree, node * 2 + 1, mid + 1, end))
        return tree[node]

def initMax(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = max(initMax(a, tree, node * 2, start, mid),
                         initMax(a, tree, node * 2 + 1, mid+1, end))
        return tree[node]

def queryMin(tree, node, start, end, left, right):
    if left > end or right < start:
        return inf
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    q1 = queryMin(tree, node * 2, start, mid, left, right)
    q2 = queryMin(tree, node * 2 + 1, mid+1, end, left, right)
    return min(q1, q2)

def queryMax(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    q1 = queryMax(tree, node * 2, start, mid, left, right)
    q2 = queryMax(tree, node * 2 + 1, mid+1, end, left, right)
    return max(q1, q2)


initMin(arr, min_tree, 1, 0, n-1)
initMax(arr, max_tree, 1, 0, n-1)

# def init(a, tree, node, start, end):
#     if start == end:
#         tree[node] = [ a[start], a[end] ]
#         return tree[node]
#     else:
#         mid = (start + end) // 2
#         left_min, left_max = init(a, tree, node*2, start, mid)
#         right_min, right_max = init(a, tree, node*2+1, mid+1, end)
#         tree[node] = [min(left_min, right_min), max(left_max, right_max)]
#         return tree[node]
#
# def query(tree, node, start, end, left, right):
#     if left > end or right < start:
#         return inf, 0
#     if left <= start and end <= right:
#         return tree[node]
#     mid = (start + end) // 2
#     min1, max1 = query(tree, node * 2, start, mid, left, right)
#     min2, max2 = query(tree, node * 2 + 1, mid+1, end, left, right)
#     return min(min1, min2), max(max1, max2)
#
#
# init(arr, t, 1, 0, n-1)


ans = ''
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # u, v = query(t, 1, 0, n-1, a-1, b-1)
    u, v = queryMin(min_tree, 1, 0, n-1, a-1, b-1), queryMax(max_tree, 1, 0, n-1, a-1, b-1)
    ans += (str(u) + ' ' + str(v) + '\n')

sys.stdout.write(ans)