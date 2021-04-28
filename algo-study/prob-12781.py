"""
12781 : Pizza Alvoloc
"""
# 피자 4등분
import sys

# 1. 가장자리 한점을 선택 (같은 점 X)
# 2. 첫번째 두번째 연결, 세번째 네번째 연결
# 3. 두 선분으로 피자 자름

# x1, y1, x2, y2, x3, y3, x4, y4 = sys.stdin.readline().split(" ")
# sys.stdin 입력은 value error 발생 (아마 마지막에 \n 들어가서 그랬던 것 같다...;;)
x1, y1, x2, y2, x3, y3, x4, y4 = input().split()
p1 = [int(x1), int(y1)]
p2 = [int(x2), int(y2)]
p3 = [int(x3), int(y3)]
p4 = [int(x4), int(y4)]


def ccw(a, b, c):
    ret = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    ret -= (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

    if ret < 0:  # 시계
        return -1
    elif ret == 0:  # 직선
        return 0
    else:
        return 1  # 반시계


# 교차해야만 4조각
# p1, p2, p3, p4 = points[:2], points[2:4], points[4:6], points[6:8]

if ccw(p1, p2, p3) * ccw(p1, p2, p4) < 0 and \
        ccw(p3, p4, p1) * ccw(p3, p4, p2) < 0:
    print(1)
else:
    print(0)
