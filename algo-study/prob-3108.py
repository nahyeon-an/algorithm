"""
3108 : 로고
더 많이 세고 있다
"""
import sys

n = int(sys.stdin.readline())
rect = [None for _ in range(n)]
zeros = [] # (0,0) 을 꼭짓점으로 가지는 사각형 번호
x = []
y = []
# 항상 x1, y1 < x2, y2
for i in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    rect[i] = (x1, y1, x2, y2)
    x += [x1, x2]
    y += [y1, y2]
    if (x1 == 0 and y1 == 0) or (x1 == 0 and y2 == 0) or (x2 == 0 and y1 ==0) or (x2 == 0 and y2 == 0):
        zeros.append(i)

visit = [False for _ in range(n)]
# 직사각형 사이에 교점이 존재하면 이동 가능
def dfs(here):
    """
    rect[here] 직사각형부터 탐색
    """
    visit[here] = True

    x1, y1, x2, y2 = rect[here]
    ret = 1

    for i in range(n):
        if i != here and not visit[i]:
            xs, ys, xl, yl = rect[i]
            # 겹치지 않는 조건을 아직 다 못 찾았다..
            if (xs < x1 < xl) and (xs < x2 < xl) and (ys < y1 < yl) and (ys < y2 < yl):
                continue
            if (x1 < xs < x2) and (x1 < xl < x2) and (y1 < ys < y2) and (y1 < yl < y2):
                continue
            if xs < x1 and xl > x2 and ys < y1 and yl > y2:
                continue
            if ys > y2 or yl < y1 or xs > x2 or xl < x1:
                continue
            ret += dfs(i)
    return ret

ans = 0
# print(sorted(x))
# print(sorted(y))
# 최초에 (0, 0) 이 꼭짓점에 존재하는 사각형들은 바로 그릴 수 있음
# 이들과 붙어있는 사각형도 바로 그릴 수 있음
# 이 사각형들은 visit = True 로 바꾸어주고 시작해야 함
for i in zeros:
    dfs(i)

for i in range(n):
    if not visit[i]:
        dfs(i)
        ans += 1

print(ans)
