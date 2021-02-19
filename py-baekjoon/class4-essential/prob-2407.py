# 2407 : 조합
n, m = input().split(" ")
n = int(n)
m = int(m)

if n//2 < m:
    m = n - m

ans = 1
for div in range(1, m+1):
    ans *= n
    n -= 1
    ans //= div # / 로 연산하는 순간 실수 오차범위 발생함

print(ans)