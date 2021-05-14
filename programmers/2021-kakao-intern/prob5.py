"""

"""
def dfs(here, visit, adj, num):
    visit[here] = True
    ret = num[here]
    for nex in adj[here]:
        if not visit[nex]:
            ret += dfs(nex, visit, adj, num)
    return ret

def solution(k, num, links):
    if k == 1:
        return sum(num)

    n = len(num)

    g = { i: set() for i in range(n) }
    edge = []
    for i in range(n):
        if links[i][0] != -1:
            edge.append([i, links[i][0]])
            g[i].add(links[i][0])
            g[links[i][0]].add(i)
        if links[i][1] != -1:
            edge.append([i, links[i][1]])
            g[i].add(links[i][1])
            g[links[i][1]].add(i)

    totMax = 100000009
    from itertools import combinations
    from copy import deepcopy
    for c in combinations(edge, k-1):
        val = []
        tree = deepcopy(g)
        for i in range(k-1):
            if c[i][0] in tree and c[i][1] in tree[c[i][0]]:
                tree[c[i][0]].remove(c[i][1])
            if c[i][1] in tree and c[i][0] in tree[c[i][1]]:
                tree[c[i][1]].remove(c[i][0])
        for i in range(k-1):
            v = [False for _ in range(n)]
            val.append(dfs(c[i][0], v, tree, num))
            v = [False for _ in range(n)]
            val.append(dfs(c[i][1], v, tree, num))
        if max(val) < totMax:
            totMax = max(val)

    return totMax


if __name__ == "__main__":
    ret = solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
                   [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]])
    print(ret)
    # 40
    ret = solution(1, [6, 9, 7, 5],
                   [[-1, -1], [-1, -1], [-1, 0], [2, 1]])
    print(ret)
    # 27
    ret = solution(2, [6, 9, 7, 5],
                   [[-1, -1], [-1, -1], [-1, 0], [2, 1]])
    print(ret)
    # 14
    ret = solution(4, [6, 9, 7, 5],
                   [[-1, -1], [-1, -1], [-1, 0], [2, 1]])
    print(ret)
    # 9