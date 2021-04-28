"""
11758 : CCW
"""
import sys

p1 = list(map(int, sys.stdin.readline().split(" ")))
p2 = list(map(int, sys.stdin.readline().split(" ")))
p3 = list(map(int, sys.stdin.readline().split(" ")))

def ccw(p1, p2, p3):
    ret = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
    ret -= (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])

    if ret < 0:  # 시계
        return -1
    elif ret == 0:  # 직선
        return 0
    else:
        return 1  # 반시계

print( ccw(p1, p2, p3) )