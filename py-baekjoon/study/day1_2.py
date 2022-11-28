import sys
import heapq

N = int(sys.stdin.readline())

heap = []
ans = ""
for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if not heap:
            ans += "0" + "\n"
            continue
        mini = heapq.heappop(heap)
        ans += str(mini[1]) + "\n"
    else:
        heapq.heappush(heap, (abs(x), x))

sys.stdout.write(ans)
