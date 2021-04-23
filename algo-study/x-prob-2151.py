"""
2151 : 거울 설치
"""
from collections import deque
import sys

n = int(sys.stdin.readline())
board = []
door = []

for i in range(n):
    line = sys.stdin.readline()
    board.append([c for c in line[:-1]])
    for j in range(len(line)):
        if line[j] == '#':
            door.append([i, j])  # 문의 위치 i행 j열

dq = deque()
dq.append(door[0])
visit = [door[0]]

board[door[0][0]][door[0][1]] = '*'

ans = 0
flag = False

prev = [[ -1 for _ in range(n) ] for _ in range(n)]

# 방향 (위 오 아 왼)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while len(dq) > 0:
    cur = dq.popleft()

    print(cur)

    if cur[0] == door[1][0] and cur[1] == door[1][1]:
        flag = True
        startx = door[0][0]
        starty = door[0][1]

        for p in prev:
            print(p)
        print("시작 :", startx, starty)
        print("도착 :", cur[0], cur[1])

        while True:
            if prev[cur[0]][cur[1]] == -1:
                break

            posx = prev[cur[0]][cur[1]][0]
            posy = prev[cur[0]][cur[1]][1]

            print(posx, posy)

            if posx == startx and posy == starty:
                print("종료 :", posx, posy)
                break

            ans += 1

            cur[0] = posx
            cur[1] = posy

        break

    for j in range(len(board[cur[0]])):
        if j == cur[1]:
            continue
        if [cur[0], j] in visit:
            continue
        #  * 거르기 -> 문제 상황
        """
5
#!..!
**...
!!..!   -> 첫번째 !에서 이전 *에서 걸려서 4,0이 안 담김
.*..*
!!..#
        """
        if board[cur[0]][j] == '*':
            break
        if board[cur[0]][j] == '#' and board[cur[0]][cur[1]] == '!':
            dq.append([cur[0], j])
            visit.append([cur[0], j])
            prev[cur[0]][j] = cur
            break
        if board[cur[0]][j] == '!':
            dq.append([cur[0], j])
            visit.append([cur[0], j])
            prev[cur[0]][j] = cur

    for j in range(n):
        if j == cur[0]:
            continue
        if [j, cur[1]] in visit:
            continue
        # * 거르기
        if board[j][cur[1]] == '*':
            break
        if board[j][cur[1]] == '#' and board[cur[0]][cur[1]] == '!':
            dq.append([j, cur[1]])
            visit.append([j, cur[1]])
            prev[j][cur[1]] = cur
            break
        if board[j][cur[1]] == '!':
            dq.append([j, cur[1]])
            visit.append([j, cur[1]])
            prev[j][cur[1]] = cur

# print(visit[1:-1])

if not flag:
    print(0)
else:
    print(ans)