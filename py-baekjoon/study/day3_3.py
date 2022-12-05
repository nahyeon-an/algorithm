# 7662 : 이중 우선순위 큐
"""
삭제
- 명령에 따라 가장 높은 or 낮은 데이터 삭제

삽입

Q -> 정수 자체가 우선순위
연산 처리 후 Q 의 데이터중 최댓값 최솟값 찾기
"""

import sys
import heapq

# TC
T = int(sys.stdin.readline())
ans = ""
for _ in range(T):
    # Q 에 적용할 연산의 개수 (~ 10^6)
    k = int(sys.stdin.readline())

    heap = []

    for _ in range(k):
        operation, n = sys.stdin.readline().split()
        n = int(n)

        if operation == 'I':
            heapq.heappush(heap, n)
        else:
            if not heap:
                continue

            if n == 1:
                removed = max(heap)
                heap.remove(removed)
            else:
                removed = heapq.heappop(heap)

    if not heap:
        ans += "EMPTY" + "\n"
    else:
        ans += f"{max(heap)} {min(heap)}" + "\n"

sys.stdout.write(ans)
