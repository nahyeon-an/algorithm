"""
8982 : 수족관 1
"""
import sys

n = int(sys.stdin.readline())  # ~ 5,000 & 짝수

stick = []
c, r = map(int, sys.stdin.readline().split())
for i in range(n//2 - 1):
    # 시계 반대 방향
    c1, r1 = map(int, sys.stdin.readline().split())
    c2, r2 = map(int, sys.stdin.readline().split())
    for j in range(c1, c2):
        stick.append(r1)
c, r = map(int, sys.stdin.readline().split())

# print(stick)

k = int(sys.stdin.readline())
hole = []  # 구멍이 난 스틱의 인덱스
for i in range(k):
    c1, r1, c2, r2 = map(int, sys.stdin.readline().split())
    hole += list(range(c1, c2))

# print(hole)

water = [0 for _ in range(len(stick))]  # 빠져나간 물
for i in range(len(hole)):
    x = hole[i]
    height = stick[x]
    water[x] = height  # x번 스틱은 물이 모두 사라짐

    # 구멍 x 기준으로 왼쪽 오른쪽 검사
    for j in range(x-1, -1, -1):
        height = min(height, stick[j])
        water[j] = max(water[j], height)

    height = stick[x]
    for j in range(x+1, len(stick)):
        height = min(height, stick[j])
        water[j] = max(water[j], height)

# print(water)
ans = 0
for r, w in zip(stick, water):
    ans += (r-w)

print(ans)

# 출력 : 구멍으로 물이 빠져나간 후 수족관에 남은 물의 양