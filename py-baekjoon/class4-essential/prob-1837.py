# 1837 : 암호 제작
p, k = input().split(" ")
p = p  # <= 10^100
k = int(k)


def mod(s, p):
    ret = 0
    for i in range(len(s)):
        ret = (ret * 10 + (ord(s[i]) - ord('0'))) % p
    return ret

# 에라토스테네스의 체 : 소수 구하기
prime = set(range(2, k + 1))
for i in range(2, k+1):
    if i in prime:
        prime -= set(range(2*i, k+1, i))

flag = True
ans = 0
if mod(p, 2) == 0 and 2 < k:
    flag = False
    ans = 2
else:
    for div in range(3, k, 2):
        if div not in prime:
            continue
        if mod(p, div) == 0:
            flag = False
            ans = div
            break

if flag:
    print("GOOD")
else:
    print("BAD", ans)
