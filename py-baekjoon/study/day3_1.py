# 1389 : 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389
import sys

# N : 유저의 수 (2 ~ 100)
# M : 친구 관계의 수 = 엣지 수 (1 ~ 5000)
N, M = map(int, sys.stdin.readline().split())

inf = 5001

friends = [[inf for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    friends[a][b] = 1
    friends[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if friends[i][j] > friends[i][k] + friends[k][j]:
                friends[i][j] = friends[i][k] + friends[k][j]

tot_sum = inf
ans = 0
for i in range(1, N + 1):
    if sum(friends[i][1:i] + friends[i][i + 1:]) < tot_sum:
        tot_sum = sum(friends[i][1:i] + friends[i][i + 1:])
        ans = i

sys.stdout.write(str(ans))
