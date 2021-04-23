"""
1956 : 운동
"""
# g[i][i] = 0으로 초기화하지 않음으로써 사이클이 존재하는 경우에만 값이 할당됨
import sys

v, e = sys.stdin.readline().split(" ")
v = int(v)  # 최대 400 -> 400 ^2 = 1600, floyd
e = int(e)

inf = 1600000000
g = [[inf for _ in range(v+1)] for _ in range(v+1)]

# 최소 사이클의 도로 길이 합
# 최단경로 찾기 문제..
for i in range(e):
    a, b, c = sys.stdin.readline().split(" ")
    # a번 마을 -> b번 마을 가는 도로 c 존재
    a, b, c = int(a), int(b), int(c)
    g[a][b] = c

# 가중치의 최소 합
# 불가능하면 -1
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if g[i][j] > g[i][k] + g[k][j]:
                g[i][j] = g[i][k] + g[k][j]

mini = inf
for i in range(1, v+1):
    if g[i][i] < mini:
        mini = g[i][i]

if mini == inf:
    print(-1)
else:
    print(mini)
