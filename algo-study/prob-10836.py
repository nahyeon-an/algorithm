"""
10836 : 여왕벌
"""

import sys

# m 700, n 10 ^ 6
m, n = sys.stdin.readline().split(" ")
m = int(m)

edge = [1 for _ in range(2*m - 1)]

for i in range(int(n)):
    zero, one, two = sys.stdin.readline().split(" ")
    zero = int(zero)
    one = int(one)
    two = int(two)

    for j in range(zero, zero+one):
        edge[j] += 1

    for j in range(zero+one, 2*m - 1):
        edge[j] += 2


sys.stdout.write(" ".join(list(map(str, edge[m-1:]))))
sys.stdout.write("\n")
for i in range(m-2, -1, -1):
    for j in range(m):
        if j == 0:
            sys.stdout.write(str(edge[i]) + " ")
        else:
            sys.stdout.write(str(edge[m-1:][j]) + " ")
    sys.stdout.write("\n")