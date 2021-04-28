"""
4991 : 로봇 청소기
"""
import sys

w, h = sys.stdin.readline()[:-1].split(" ")
w, h = int(w), int(h)

while w != 0 or h != 0:
    board = []
    start = []

    dirty = 0
    for i in range(h):
        board.append(list(sys.stdin.readline()[:-1]))
        for j in range(w):
            if board[i][j] == 'o':
                start = [i, j]
            if board[i][j] == '*':
                dirty += 1

    # dp[pos][dirty] : pos 위치에서 dirty 집합을 방문한 이동 횟수
    #

    w, h = sys.stdin.readline()[:-1].split(" ")
    w, h = int(w), int(h)