# 2623 : 음악 프로그램 (위상 정렬)

import sys
from collections import deque

n, m = sys.stdin.readline().split(" ")
n = int(n)  # 가수의 수
m = int(m)  # 보조 pd 수

adjList = dict()
for i in range(1, n+1):
    adjList[i] = []

ind = [0 for _ in range(n+1)]
for i in range(m):
    rule = sys.stdin.readline().split(" ")
    rule = rule[1:]
    for j in range(len(rule)-1):
        adjList[int(rule[j])].append(int(rule[j+1]))
        ind[int(rule[j+1])] += 1

dq = deque()
for i in range(1, n+1):
    if ind[i] == 0:
        dq.append(i)

visit = []
ans = ""
cnt = 0
while len(dq) > 0:
    cur = dq.popleft()
    ans += str(cur) + "\n"
    cnt += 1
    for nex in adjList[cur]:
        ind[nex] -= 1
        if ind[nex] == 0:
            dq.append(nex)

if cnt == n:
    sys.stdout.write(ans)
else:
    sys.stdout.write("0")