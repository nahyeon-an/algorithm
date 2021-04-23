"""
12886 : 돌 그룹
"""
from collections import deque
import sys

a, b, c = sys.stdin.readline().split(" ")
a, b, c = int(a), int(b), int(c)

if (a+b+c) % 3 != 0:
    print(0)
    sys.exit(0)

# 1. 크기가 같지 않은 두 그룹을 선택 -> 어떤 순서로 선택할 것인가..?
# 2. 돌의 개수가 작은 쪽 = X, 큰 쪽 = Y
# 3. X의 돌의 개수를 X+X, Y 의 돌의 개수를 Y-X 로 만듦
dq = deque()
dq.append([a, b, c])

# visit[a][b] -> a, b 를 이용하여 합을 만들었다
# max = total + 1 = 1501 ( 각 값이 맥스가 500 )
visit = [[False for _ in range(10000)] for _ in range(10000)]

# visit을 사용해줘야함 => -1인 경우를 찾기 위해
while len(dq) > 0:
    cur = dq.popleft()

    # 이 부분 dq.append 할 때 검사하도록 변경하기.
    # 여기가 시간 좀 잡아먹는 것 같다
    if visit[cur[0]][cur[1]]:
        continue
    visit[cur[0]][cur[1]] = True

    if cur[0] == cur[1] and cur[1] == cur[2]:
        print(1)
        sys.exit(0)

    if cur[0] != cur[1]:
        if cur[0] > cur[1]:
            dq.append([cur[0]-cur[1], 2 * cur[1], cur[2]])
        else:
            dq.append([2 * cur[0], cur[1]-cur[0], cur[2]])

    if cur[0] != cur[2]:
        if cur[0] > cur[2]:
            dq.append([cur[0]-cur[2], cur[1], 2 * cur[2]])
        else:
            dq.append([2 * cur[0], cur[1], cur[2]-cur[0]])

    if cur[1] != cur[2]:
        if cur[1] > cur[2]:
            dq.append([cur[0], cur[1]-cur[2], 2 * cur[2]])
        else:
            dq.append([cur[0], 2 * cur[1], cur[2]-cur[1]])

# 모든 그룹의 돌의 개수가 같아질 수 있으면 1 아니면 0 출력
print(0)