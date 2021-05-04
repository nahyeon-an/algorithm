"""
2533 : 사회망 서비스
"""
import sys

# <= 10^6
n = int(sys.stdin.readline())

graph = dict()
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

# dp[i][j] : i번 노드가 0(얼리어댑터 아님) or 1(얼리어댑터이다)일 때
# 얼리어댑터의 수?
dp = [[-1 for _ in range(2)] for _ in range(n+1)]
visit = [ False for _ in range(n+1) ]

def isFinished():
    for i in range(1, n+1):
        if not visit[i]:
            return False
    return True

# flag : 얼리어댑터이다/아니다
# here : 현재 노드
# 어렵다...
def solve(here, flag):
    # 모든 노드를 방문했을 때 -> 이게 이상한 것 같기도 하다
    # base case가 이상한 것 같다...
    if isFinished():
        print(here, flag)
        if flag == 1:
            return 1
        else:
            return 99

    if dp[here][flag] != -1:
        return dp[here][flag]

    ret = 0
    if flag == 1:
        for nex in graph[here]:
            if not visit[nex]:
                visit[nex] = True
                ret += min(solve(nex, 0), solve(nex, 1))
    else:
        for nex in graph[here]:
            if not visit[nex]:
                visit[nex] = True
                ret += solve(nex, 1)
    dp[here][flag] = ret
    # print(here, flag, ret)
    return ret

ans = min(solve(1, 0), solve(1, 1))
print(ans)

