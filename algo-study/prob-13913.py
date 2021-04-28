"""
13913 : 숨바꼭질 4 (bfs)
1 0 -> 40%
0 5 -> 57%
둘 다 마지막에 출력문제
하나가 0인 경우..
"""
from collections import deque
import sys

# 0 ~ 100000 -> n or nlogn
n, k = sys.stdin.readline()[:-1].split(" ")
n, k = int(n), int(k)

# x -> x-1, x+1, 2*x
dq = deque()
dq.append(n)

visit = [-1 for _ in range(100001)]

while len(dq) > 0:
    cur = dq.popleft()

    if cur == k:
        temp = cur
        ret = deque()
        while temp != n:
            ret.appendleft(str(temp))
            temp = visit[temp]
        ret.appendleft(str(temp))
        sys.stdout.write(str(len(ret)-1) + "\n")
        sys.stdout.write(" ".join(ret) + "\n")
        break

    if (cur+1) <= 100000 and visit[cur + 1] == -1:
        dq.append(cur + 1)
        visit[cur + 1] = cur
    if (cur-1) >= 0 and visit[cur - 1] == -1:
        dq.append(cur - 1)
        visit[cur - 1] = cur
    if 2*cur <= 100000 and visit[2 * cur] == -1:
        dq.append(2 * cur)
        visit[2 * cur] = cur