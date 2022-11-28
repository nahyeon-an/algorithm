import sys

T = int(sys.stdin.readline())  # tc 수

ans = ""
for i in range(T):
    # M : 배추 밭의 가로 길이 (1~50) -> 열의 개수
    # N : 배추 밭의 세로 길이 (1~50) -> 행의 개수
    # K : 배추 위치 개수 (1~2500)
    # n^2
    M, N, K = map(int, sys.stdin.readline().split(" "))
    matrix = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split(" "))
        matrix[Y][X] = 1

    # 인접 노드 방문
    cnt = 0
    for r in range(N):
        for c in range(M):
            if matrix[r][c] == 1:
                stack = [(r, c)]

                while stack:
                    r, c = stack.pop()
                    matrix[r][c] = 0

                    if r - 1 >= 0 and matrix[r - 1][c] == 1:
                        stack.append((r - 1, c))
                    if r + 1 < N and matrix[r + 1][c] == 1:
                        stack.append((r + 1, c))
                    if c - 1 >= 0 and matrix[r][c - 1] == 1:
                        stack.append((r, c - 1))
                    if c + 1 < M and matrix[r][c + 1] == 1:
                        stack.append((r, c + 1))

                cnt += 1

    ans += str(cnt) + "\n"

# 25%
sys.stdout.write(ans)
