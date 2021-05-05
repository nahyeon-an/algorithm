"""
2533 : 사회망 서비스
메모리 초과 조심..
"""
import sys

# <= 10^6
n = int(sys.stdin.readline())
sys.setrecursionlimit(10 ** 9)

graph = dict()
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

tree = [[] for _ in range(n + 1)]
v = [False for _ in range(n + 1)]
# 왜 반드시 단방향으로 트리를 만들어줘야 통과가 되는 걸까..?
# visit으로 했을 때 True 표시되면 안 가니까 될거같았는데 안되었다..
def make_tree(here):
    v[here] = True
    for nex in graph[here]:
        if not v[nex]:
            tree[here].append(nex)
            make_tree(nex)

make_tree(1)
# del graph

# dp[i][j] : i번 노드가 0(얼리어댑터 아님) or 1(얼리어댑터이다)일 때
# 얼리어댑터의 수?
dp = [[-1 for _ in range(2)] for _ in range(n + 1)]

# flag : 얼리어댑터이다/아니다
# here : 현재 노드
print("\n---solve---")
def solve(here, flag):
    if dp[here][flag] != -1:
        return dp[here][flag]

    if flag == 1:
        ret = 1
        for nex in tree[here]:
            ret += min(solve(nex, 0), solve(nex, 1))
    else:
        ret = 0
        for nex in tree[here]:
            ret += solve(nex, 1)
    dp[here][flag] = ret
    print(here, flag, ret)
    return ret

visit = [False for _ in range(n+1)]
print("\n---dfs---")
def dfs(here, flag):
    if dp[here][flag] != -1:
        return dp[here][flag]

    if flag == 1:
        ret = 1
        for nex in graph[here]:
            if not visit[nex]:
                visit[nex] = True
                ret += min(solve(nex, 0), solve(nex, 1))
    else:
        ret = 0
        for nex in graph[here]:
            if not visit[nex]:
                ret += solve(nex, 1)
                visit[nex] = True

    dp[here][flag] = ret
    print(here, flag, ret)
    return ret


ans = min(solve(1, 0), solve(1, 1))
print(ans)
