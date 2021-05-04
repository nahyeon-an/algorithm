"""
13460 : 구슬 탈출 2
"""
from collections import deque
import sys

# 3 ~ 10
n, m = map(int, sys.stdin.readline().strip().split())

blue = []
red = []
dest = []

# board[n][m]
board = []
for i in range(n):
    line = sys.stdin.readline().strip()
    board.append(line)
    for j in range(m):
        if line[j] == 'B':
            blue = [i, j]
        elif line[j] == 'R':
            red = [i, j]
        elif line[j] == 'O':
            dest = [i, j]

"""
. : 빈 칸
# : 장애물
O : 구멍
R : 빨간 구슬 위치 -> 구멍에 빠지면 성공
B : 파란 구슬 위치 -> 구멍에 빠지면 실패
빨간, 파란 -> 동시에 같은 칸에 불가능

위 오 아 왼 기울이기 -> 구슬이 움직이지 않을 때까지 = 빈칸이면 계속 이동
기울일때마다 두 구슬이 동시에 움직인다..
"""

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

dq = deque()
dq.append(red)

"""
red == dest 일 때 종료
red 전에 blue 가 dest 에 도달하면 
"""

while len(dq) > 0:
    cur = dq.popleft()

    posr = cur[0]
    posc = cur[1]

    while board[posr][posc] != '#':
        for i in range(4):
            posr += dr[i]
            posc += dc[i]