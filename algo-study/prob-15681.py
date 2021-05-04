"""
15681 : 트리와 쿼리
"""
import sys
sys.setrecursionlimit(10**7)

# n, q <= 10^6
# r <= n
# 정점의 수, 루트 번호, 쿼리 수
n, r, q = map(int, sys.stdin.readline().split())

graph = dict()
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)

visit = [ False for _ in range(n+1) ]
# dp[n] : 노드 n의 서브 점들의 개수
dp = [0 for _ in range(n+1)]

def query(g, node):
    ret = dp[node]
    if ret != 0:
        return ret

    # 자기 자신
    ret = 1
    for nex in g[node]:
        if not visit[nex]:
            visit[nex] = True
            ret += query(g, nex)
    dp[node] = ret
    return ret

visit[r] = True
query(graph, r)

ans = ""
for _ in range(q):
    u = int(sys.stdin.readline().strip())
    ans += str(dp[u]) + "\n"

sys.stdout.write(ans)

# 정점 U를 루트로 하는 서브트리에 속한 정점의 수