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
dq.append([door[0], -1])  # 좌표, 방향
visit = [door[0]]

prev = [[ -1 for _ in range(n) ] for _ in range(n)]

# 방향 (위 오 아 왼)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

ans = 0
while len(dq) > 0:
    cur = dq.popleft()

    if cur[0] == door[1]:
        while True:
            if prev[cur[0][0]][cur[0][1]] == -1:
                break

            posx = prev[cur[0][0]][cur[0][1]][0]
            posy = prev[cur[0][0]][cur[0][1]][1]

            if posx == door[0][0] and posy == door[0][1]:
                break

            cur[0] = [posx, posy]
            ans += 1
        break

    dir = cur[1]

    # 이전에 온 방향 제외하고 사방으로 이동 가능한지 확인
    for i in range(4):
        if dir != -1 and i == (dir + 2) % 4:
            continue

        posr = cur[0][0]
        posc = cur[0][1]
        while True:
            posr += dr[i]
            posc += dc[i]
            if posr >= n or posc >= n or posr < 0 or posc < 0:
                break
            if posr == door[1][0] and posc == door[1][1]:
                dq.appendleft([[posr, posc], i])
                prev[posr][posc] = cur[0]
                break
            if board[posr][posc] == '*':
                break
            if board[posr][posc] == '!':
                if prev[posr][posc] == -1:
                    dq.append([[posr, posc], i])
                    prev[posr][posc] = cur[0]

print(ans)