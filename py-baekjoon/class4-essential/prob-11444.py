"""
11444 : 피보나치 수 6
"""
import sys

mod = 1000000007

n = int(sys.stdin.readline())

def multiply(a, b):
    size = len(a)
    ret = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                ret[i][j] += (a[i][k] * b[k][j])
            ret[i][j] %= mod

    return ret

ans = [
    [1, 0],
    [0, 1]
]

m = [
    [1, 1],
    [1, 0]
]

while n > 0:
    if n % 2 == 1:
        ans = multiply(ans, m)
    m = multiply(m, m)
    n //= 2

print(ans[0][1])