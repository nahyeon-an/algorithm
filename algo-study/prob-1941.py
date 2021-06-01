"""
1941 : 소문난 칠공주
"""
import sys

n = 5

board = []
s = []
y = []
for i in range(n):
    line = sys.stdin.readline().strip()
    for j in range(n):
        board += line[j]
        if line[j] == 'S':
            s.append(i * n + j)
        else:
            y.append(i * n + j)

if len(s) < 4:
    print(0)
    sys.exit(0)

def solve(e):
    if visit[e]:
        return

    visit[e] = True

    if e % n != n-1 and e + 1 in visit:
        solve(e+1)
    if e % n != 0 and e - 1 in visit:
        solve(e-1)
    if e // n != 0 and e - n in visit:
        solve(e-n)
    if e // n != n-1 and e+n in visit:
        solve(e+n)


from itertools import combinations

ans = 0
for i in range(4, 8):
    tmp_s = list(combinations(s, i))
    tmp_y = list(combinations(y, 7-i))

    for comb_s in tmp_s:
        for comb_y in tmp_y:
            visit = {c: False for c in comb_s + comb_y}
            solve(comb_s[0])

            cnt = 0
            for val in visit.values():
                if val:
                    cnt += 1

            if cnt == 7:
                ans += 1

print(ans)