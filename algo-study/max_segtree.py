import math

def initMax(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
        return tree[node]
    else:
        tree[node] = max(initMax(a, tree, node * 2, start, (start+end)//2),
                         initMax(a, tree, node * 2 + 1, (start+end)//2+1, end))
        return tree[node]

def queryMax(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    q1 = queryMax(tree, node * 2, start, (start+end)//2, left, right)
    q2 = queryMax(tree, node * 2 + 1, (start+end)//2+1, end, left, right)
    if q1 == 0:
        return q2
    elif q2 == 0:
        return q1
    else:
        return max(q1, q2)


if __name__ == '__main__':
    n = 10
    arr = [75, 30, 100, 38, 50, 51, 52, 20, 81, 5]
    max_tree = [0] * (pow(2, math.ceil(math.log(n, 2)) + 1) - 1)

    initMax(arr, max_tree, 1, 0, n-1)

    print(queryMax(max_tree, 1, 0, n-1, 0, 9))
    print(queryMax(max_tree, 1, 0, n - 1, 3, 8))
    print(queryMax(max_tree, 1, 0, n - 1, 2, 4))
    print(queryMax(max_tree, 1, 0, n - 1, 1, 5))