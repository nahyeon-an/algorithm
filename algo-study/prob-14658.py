"""
14658 : 하늘에서 ~
"""
import sys

n, m, l, k = map(int, sys.stdin.readline().split())

stars = []
for _ in range(k):
    c, r = map(int, sys.stdin.readline().split())
    stars.append([r, c])

ans = 0

for i in range(k):
    for j in range(k):
        cnt = 0
        for t in range(k):
            posr, posc = stars[t]
            if stars[i][0] <= posr <= stars[i][0] + l and \
                stars[j][1] <= posc <= stars[j][1] + l:
                cnt += 1
        ans = max(ans, cnt)

print(k - ans)
