"""
2186 : 문자판
"""
from collections import deque
import sys

n, m, k = sys.stdin.readline()[:-1].split(" ")
# 1~100, 1~100, 1~5
# n * m 문자판
n, m, k = int(n), int(m), int(k)

board = []
for _ in range(n):
    board.append(sys.stdin.readline()[:-1])

# 1 ~ 80 길이의 영단어
word = sys.stdin.readline()[:-1]

# 상하좌우로 k개의 칸만 이동 가능
# 반드시 한 칸 이상 이동, 같은 칸을 여러번 방문 가능

# dp[i] : word의 처음 부터 i까지 이동가능한 경로 수
dp = [0 for _ in range(len(word))]

# board 에 word 의 모든 글자가 존재하는지 확인
for c in word:
    flag = False
    for b in board:
        if c in b:
            flag = True
            break
    if not flag:
        print(0)
        sys.exit(0)

# word[0]이 board에서 어디 위치하는지 찾기
dq = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == word[0]:
            dq.append([i, j, 0])
            dp[0] += 1

# 메모리 초과
while len(dq) > 0:
    cur = dq.popleft()
    nex = cur[2] + 1

    if nex == len(word):
        continue

    for dk in range(1, k+1):
        # 위
        if cur[0]-dk >=0 and board[cur[0]-dk][cur[1]] == word[nex]:
            dq.append([cur[0]-dk, cur[1], nex])
            dp[nex] += 1
        # 아래
        if cur[0]+dk < n and board[cur[0] + dk][cur[1]] == word[nex]:
            dq.append([cur[0] + dk, cur[1], nex])
            dp[nex] += 1
        # 왼쪽
        if cur[1]-dk >= 0 and board[cur[0]][cur[1]-dk] == word[nex]:
            dq.append([cur[0], cur[1] - dk, nex])
            dp[nex] += 1
        # 오른쪽
        if cur[1]+dk < m and board[cur[0]][cur[1]+dk] == word[nex]:
            dq.append([cur[0], cur[1] + dk, nex])
            dp[nex] += 1

print(dp[len(word)-1])
