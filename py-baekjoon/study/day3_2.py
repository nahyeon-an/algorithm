# 1780 : 종이의 개수
# https://www.acmicpc.net/problem/1780

import sys

# 1 ~ 3^7 = 81 * 27 = 2187
N = int(sys.stdin.readline())
board = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)
ans = [0, 0, 0]  # -1, 0, 1


def is_same_elements(m):
    size = len(m)
    num = m[0][0]
    for i in range(size):
        for j in range(size):
            if m[i][j] != num:
                return None

    if num == m[0][0]:
        return num  # 종이의 숫자


def divide_and_conquer(m):
    ret = is_same_elements(m)
    if ret is not None:
        return ret

    size = len(m)
    step = size // 3

    for k in range(0, size, step):
        for c in range(0, size, step):
            divided_map = []
            for r in range(k, k + step):
                divided_map.append(m[r][c:c + step])
            n = divide_and_conquer(divided_map)

            if n is None:
                continue

            ans[n + 1] += 1


n = divide_and_conquer(board)
if n is not None:
    ans[n+1] += 1
sys.stdout.write("\n".join(map(str, ans)))
