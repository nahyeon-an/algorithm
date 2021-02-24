# 1629 : 곱셈

a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

ans = 1
while b > 1:
    if b % 2 == 0:
        b //= 2
        a *= a
    else:
        b //= 2
        ans *= a
        ans %= c
        a *= a
    a %= c

ans *= a
print(ans % c)