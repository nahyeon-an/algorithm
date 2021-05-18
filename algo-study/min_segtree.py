import math

def initMin(a, tree, node, start, end):
    """
    주어진 데이터로 세그먼트 트리를 채운다.
    구간합 세그먼트 트리
    node : 노드 번호
    a[start] ~ a[end] 의 합을 저장함
    """
    if start == end:
        # leaf node
        tree[node] = a[start]
        return tree[node]
    else:
        tree[node] = min(initMin(a, tree, node * 2, start, (start+end) // 2),
                     initMin(a, tree, node * 2 + 1, (start+end)//2 + 1, end))
        return tree[node]

def queryMin(tree, node, start, end, left, right):
    """
    노드번호가 node일때 a[start] ~ a[end]를 담당
    쿼리 범위 left ~ right
    """
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    q1 = queryMin(tree, node * 2, start, (start+end)//2, left, right)
    q2 = queryMin(tree, node * 2 + 1, (start+end)//2+1, end, left, right)
    if q1 == 0:
        return q2
    elif q2 == 0:
        return q1
    else:
        return min(q1, q2)

def updateMin(tree, node, start, end, idx, val):
    """
    arr[idx] 의 값을 val로 업데이트
    """
    if idx < start or idx > end:
        return
    tree[node] = min(tree[node], val)
    if start != end:
        mid = (start + end) // 2
        updateMin(tree, 2*node, start, mid, idx, val)
        updateMin(tree, 2*node + 1, mid+1, end, idx, val)


if __name__ == '__main__':
    n = 10
    arr = [75, 30, 100, 38, 50, 51, 52, 20, 81, 5]
    min_tree = [0] * (pow(2, math.ceil(math.log(n, 2)) + 1) - 1)

    initMin(arr, min_tree, 1, 0, n-1)

    print(queryMin(min_tree, 1, 0, n-1, 0, 9))
    print(queryMin(min_tree, 1, 0, n - 1, 3, 8))
    print(queryMin(min_tree, 1, 0, n - 1, 2, 4))
    print(queryMin(min_tree, 1, 0, n - 1, 1, 5))
    print(queryMin(min_tree, 1, 0, n-1, 5, 5))
    updateMin(min_tree, 1, 0, n-1, 5, 10)
    arr[5] = 10
    print(queryMin(min_tree, 1, 0, n-1, 5, 5))