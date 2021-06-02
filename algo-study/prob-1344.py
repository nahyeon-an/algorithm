"""
1344 : 축구
"""
import sys

# [0, 100]
a = int(sys.stdin.readline()) / 100
b = int(sys.stdin.readline()) / 100

n = 18
primes = [2, 3, 5, 7, 11, 13, 17]
non_primes = set(range(n + 1)) - set(p for p in primes)

# print(non_primes)

# dp1[i] : A팀이 i번의 골을 넣는 경우의 수
# 18 C i = 17 C i + 17 C i-1

comb = [[0] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    comb[i][0] = 1
    comb[i][i] = 1

for i in range(2, n+1):
    for j in range(1, i+1):
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]

tot = 0
for sa in non_primes:
    for sb in non_primes:
        A = (a ** sa) * ((1-a)**(n - sa)) * comb[n][sa]
        B = (b ** sb) * ((1-b)**(n - sb)) * comb[n][sb]
        tot += (A * B)

# print(tot, 1-tot)
print(1-tot)

# 적어도 한 팀이 골을 소수로 득점할 확률
# 1 - 둘 다 소수로 득점하지 않을 확률