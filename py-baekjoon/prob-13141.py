"""
13141 : Ignition
mst 문제 아닐까
"""
import sys
from copy import deepcopy


def solution(i, n, graph):
    """
    i번 노드에 불을 붙였을 때, 그래프가 타는데에 걸리는 시간을 리턴
    n 은 노드 개수
    """
    from collections import deque
    dq = deque()
    dq.append(i)

    visit = [False for _ in range(n+1)]
    visit[i] = True

    while dq:
        cur = dq.popleft()
        s = sorted(graph[cur], key=lambda x: x[1])
        min_cost = s[0][1]
        print(cur, min_cost)

        for i, pair in enumerate(graph[cur]):
            if visit[pair[0]]:
                # edge cost 계속 줄여야 함
                graph[pair[0]]
                continue
            pair[1] -= min_cost
            if pair[1] <= 0:
                visit[pair[0]] = True
                dq.append(pair[0])

    print(graph)


if __name__ == '__main__':
    # 입력
    # n : 그래프 정점의 수 (2 <= <= 200), m : 간선의 수 (n-1 <= <= 20000)
    n, m = map(int, sys.stdin.readline().split())

    g = dict()
    for _ in range(m):
        # s : 시작점, e : 끝점, l : 길이 (1<=<=100)
        s, e, l = map(int, sys.stdin.readline().split())
        g.setdefault(s, [])
        g[s].append([e, l])
        g.setdefault(e, [])
        g[e].append([s, l])

    for i in range(1, n+1):
        solution(i, n, deepcopy(g))
        print()

    # 출력 : 그래프를 모두 태우는 데 걸리는 최소 시간
