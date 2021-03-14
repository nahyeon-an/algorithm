# 1005 : ACM craft
# fast io : sys.stdin.readline()
# sys.stdout.write()
# print, input 함수로 입출력 받으면 58프로에서 시간 초과 발생

import sys
from collections import deque

t = int(sys.stdin.readline())

ans = ""
while t > 0:
    n, k = sys.stdin.readline().split(" ")
    n = int(n)  # 건물 개수
    k = int(k)  # 규칙 개수
    d = [int(x) for x in input().split(" ")]  # 건물 건설에 걸리는 시간
    ind = [0 for _ in range(n)]

    adjList = dict()
    for i in range(k):
        x, y = sys.stdin.readline().split(" ")
        x = int(x) -1
        y = int(y) -1
        ind[y] += 1
        if x not in adjList:
            adjList[x] = []
        adjList[x].append(y)

    ret = [0 for _ in range(n)]
    dq = deque()
    for i in range(n):
        if ind[i] == 0:
            dq.append(i)
            ret[i] = d[i]

    w = int(sys.stdin.readline()) - 1   # 건설해야하는 건물 번호
    while len(dq) > 0:
        now = dq.popleft()
        if now == w:
            break
        if now not in adjList:
            continue
        for nex in adjList[now]:
            ind[nex] -= 1
            if ind[nex] == 0:
                if nex == w:
                    dq.appendleft(nex)
                else:
                    dq.append(nex)
            ret[nex] = max(ret[nex], ret[now] + d[nex])

    ans += str(ret[w]) + "\n"

    t -= 1

sys.stdout.write(ans)