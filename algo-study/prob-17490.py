"""
17490 : 일감호에 다리 놓기
"""
import sys

n, m, k = map(int, sys.stdin.readline().split())
snum = list(map(int, sys.stdin.readline().split()))

cut = []
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if u > v:
        u, v = v, u
    if u == 1 and v == n:
        cut.append(0)
        continue
    cut.append(u)

if m <= 1:
    sys.stdout.write('YES\n')
    sys.exit(0)

cut.sort()
# print(cut)

cnt = 0
for i in range(len(cut)-1):
    # print(snum[cut[i]:cut[i+1]])
    cnt += min(snum[cut[i]:cut[i+1]])

if cut[0] != 0:
    # print(snum[:cut[0]] + snum[cut[i+1]:])
    cnt += min(snum[:cut[0]] + snum[cut[i+1]:])
else:
    # print(snum[cut[i+1]:])
    cnt += min(snum[cut[i+1]:])

if cnt > k:
    sys.stdout.write('NO\n')
else:
    sys.stdout.write('YES\n')