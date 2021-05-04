# 기본 : 최소 힙
import heapq

heap = []
heapq.heappush(heap, (1, 2))
heapq.heappush(heap, (-2, 2))
heapq.heappush(heap, (0, -3))
heapq.heappush(heap, (0, 3))
heapq.heappush(heap, (-5, -4))

print(heap)

x = [4, 2, 0, -3, 1, 6]
heapq.heapify(x)
print(x)

jobs = [[0, 3], [1, 9], [2, 6]]
j = []
for job in jobs:
    heapq.heappush(j, [job[1], job[0]])
heapq.heapify(jobs)
print(jobs)

ret = [heapq.heappop(j) for _ in range(len(j))]
print(j)
print(ret)