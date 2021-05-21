"""
7453 : 합이 0인 네 정수
15% 틀림
반례 발견
2
0 -100 2 2
0 -4 2 4

정답: 4
오답: 2
"""
import sys

n = int(sys.stdin.readline())  # <= 4000

a, b, c, d = [], [], [], []

for _ in range(n):
    x, y, z, w = map(int, sys.stdin.readline().split())
    a.append(x)
    b.append(y)
    c.append(z)
    d.append(w)

ans = 0

arr1 = dict()
arr2 = dict()

for x in a:
    for y in b:
        arr1[x+y] = arr1.get(x+y, 0) + 1

for z in c:
    for w in d:
        ans += arr1.get(-(z+w), 0)

print(ans)

