"""
17387 : 선분 교차 2
"""
import sys

# L1
x1, y1, x2, y2 = sys.stdin.readline().split(" ")
p1 = [int(x1), int(y1)]
p2 = [int(x2), int(y2)]

# L2
x3, y3, x4, y4 = sys.stdin.readline().split(" ")
p3 = [int(x3), int(y3)]
p4 = [int(x4), int(y4)]

if p1 == p3 or p1 == p4 or \
    p2 == p3 or p2 == p4:
    print(1)
    sys.exit(0)

def ccw(a, b, c):
    ret = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    ret -= (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

    if ret > 0:  # 반시계 방향
        return 1
    elif ret == 0:  # 평행
        return 0
    else:
        return -1  # 시계 방향

if ccw(p1, p2, p3) == 0:
    if min(p1[0], p2[0]) <= p3[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= p3[1] <= max(p1[1], p2[1]):
        print(1)
        sys.exit(0)
if ccw(p1, p2, p4) == 0:
    if min(p1[0], p2[0]) <= p4[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= p4[1] <= max(p1[1], p2[1]):
        print(1)
        sys.exit(0)
if ccw(p3, p4, p1) == 0:
    if min(p3[0], p4[0]) <= p1[0] <= max(p3[0], p4[0]) and min(p3[1], p4[1]) <= p1[1] <= max(p3[1], p4[1]):
        print(1)
        sys.exit(0)
if ccw(p3, p4, p2) == 0:
    if min(p3[0], p4[0]) <= p2[0] <= max(p3[0], p4[0]) and min(p3[1], p4[1]) <= p2[1] <= max(p3[1], p4[1]):
        print(1)
        sys.exit(0)

if ccw(p1, p2, p3) * ccw(p1, p2, p4) < 0 and \
    ccw(p3, p4, p1) * ccw(p3, p4, p2) < 0:
    print(1)
else:
    print(0)