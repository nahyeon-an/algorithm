"""
10160 : 암호
올림피아드 풀이를 봤는데 무슨 소리인지 잘 모르겠다..
"""
import sys

# 암호길이, 문자의 가지수
n, k = map(int, sys.stdin.readline().split())
mod = 1000000009

e = [0 for _ in range(7)]
d = [0 for _ in range(7)]

e[0] = 1
for i in range(1, n+1):
    d[0] = (e[0] * (k-1) % mod + e[1] * (k-2) % mod + e[2] * (k-2) % mod +
            e[3] * (k-2) % mod + e[4] * (k-2) % mod + e[5] * (k-2) % mod +
            e[6] * (k-2) % mod) % mod
    d[1] = (e[0] + e[1] + e[3] + e[5] + e[6]) % mod
    d[2] = e[1]
    d[3] = (e[2] + e[4]) % mod
    d[4] = e[3]
    d[5] = e[2]
    d[6] = e[5]
    for j in range(7):
        e[j] = d[j]
    print(d, e)

ans = 0
for i in range(7):
    ans = (ans + d[i]) % mod
print(ans)