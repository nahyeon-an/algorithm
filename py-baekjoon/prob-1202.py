"""
1202 : 보석 도둑
왜 15% 시간초과일까? 나한테서는 잘만 빠르게 돌아가는데..?
"""
import sys
import heapq

n, k = map(int, sys.stdin.readline().split())

h = []
for i in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(h, [-v, m])

from bisect import bisect_left

bag = [int(sys.stdin.readline()) for _ in range(k)]
# for i in range(k):
#     c = int(sys.stdin.readline())
#     bag.append(c)

bag = sorted(bag)
# print(bag)

cnt = 0
ans = 0
while h:
    # 가격, 무게
    v, w = heapq.heappop(h)

    if cnt > k:
        break

    if bag:
        idx = bisect_left(bag, w)
        if idx < len(bag):
            bag.pop(idx)
            ans -= v
            cnt += 1

print()
print(ans)
