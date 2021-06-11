"""
1022 : 소용돌이 예쁘게 출력
"""
import sys
sys.setrecursionlimit(10**4)

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

n = max([abs(r1), abs(c1), abs(r2), abs(c2)])
# r1 += n
# c1 += n
# r2 += n
# c2 += n

# 전체를 구하지 말고 필요한 부분만 계산해야 할 것 같다
board = [[0] * (abs(c1-c2)+1) for _ in range(abs(r1-r2)+1)]

if r1 <= 0 <= r2 and c1 <= 0 <= c2:
    board[n-(r1+n)][n-(c1+n)] = 1

num = 2

for i in range(1, n+1):
    r, c = n+i-1, n+i
    while r >= n - i:
        if r1+n <= r <= r2+n and c1+n <= c <= c2+n:
            board[r-(r1+n)][c-(c1+n)] = num
        r -= 1
        num += 1
    r += 1

    c -= 1
    while c >= n - i:
        if r1+n <= r <= r2+n and c1+n <= c <= c2+n:
            board[r-(r1+n)][c-(c1+n)] = num
        c -= 1
        num += 1
    c += 1

    r += 1
    while r <= n + i:
        if r1+n <= r <= r2+n and c1+n <= c <= c2+n:
            board[r-(r1+n)][c-(c1+n)] = num
        r += 1
        num += 1
    r -= 1

    c += 1
    while c <= n + i:
        if r1+n <= r <= r2+n and c1+n <= c <= c2+n:
            board[r-(r1+n)][c-(c1+n)] = num
        c += 1
        num += 1

# for b in board:
#     print(b)

length = max([len(str(board[0][0])), len(str(board[0][abs(c1-c2)])),
              len(str(board[abs(r1-r2)][0])), len(str(board[abs(r1-r2)][abs(c1-c2)]))])

for i in range(0, abs(r1-r2)+1):
    for j in range(0, abs(c1-c2)+1):
        print(str(board[i][j]).rjust(length), end=' ')
    print()
