"""
2174 : 로봇 시뮬레이션
"""
import sys

a, b = sys.stdin.readline().split(" ")
a = int(a)
b = int(b)

n, m = sys.stdin.readline().split(" ")
n = int(n)
m = int(m)

robots = dict()

# 로봇의 초기위치와 방향
for i in range(1, n+1):
    x, y, dir = sys.stdin.readline().split(" ")
    if dir == 'N\n':
        robots[i] = [int(x), int(y), 0]
    elif dir == 'E\n':
        robots[i] = [int(x), int(y), 1]
    elif dir == 'S\n':
        robots[i] = [int(x), int(y), 2]
    elif dir == 'W\n':
        robots[i] = [int(x), int(y), 3]

# NESW = 0123
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(m):
    n, command, cnt = sys.stdin.readline().split(" ")
    n = int(n)
    cnt = int(cnt)

    print("-- ", n, command, cnt)
    if command == 'L':
        robots[n][2] -= cnt
        robots[n][2] %= 4
    elif command == 'R':
        robots[n][2] += cnt
        robots[n][2] %= 4
    elif command == 'F':
        for j in range(cnt):
            robots[n][0] += dx[robots[n][2]]
            robots[n][1] += dy[robots[n][2]]

            if robots[n][0] <= 0 or robots[n][1] <= 0 \
                    or robots[n][0] > a or robots[n][1] > b:
                print("Robot {} crashes into the wall".format(n))
                sys.exit(0)

            for key, val in robots.items():
                print(n, robots[n], key, val)
                if key == n:
                    continue
                if robots[n][0] == val[0] and robots[n][1] == val[1]:
                    print("Robot {} crashes into robot {}".format(n, key))
                    sys.exit(0)

print("OK")
