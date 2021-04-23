"""
20047 : 동전 옮기기
단어섞기와 완전히 같은 dp 문제
"""
import sys

n = int(sys.stdin.readline())  # 최대 10^4
s = sys.stdin.readline()[:-1]
t = sys.stdin.readline()[:-1]
i, j = sys.stdin.readline().split(" ")
i = int(i)
j = int(j)

# s -> t 변환 가능한가?
sub = s[:i] + s[i+1:j] + s[j+1:]
coin = [s[i], s[j]]

# dp[i][j]
# sub의 앞 i개 와 coin의 앞 j개를 이용해 t의 i+j 개를 만들 수 있는지
dp = [[False for _ in range(len(coin)+1)] for _ in range(len(sub)+1)]

if t[0] == sub[0]:
    dp[1][0] = True

if t[0] == coin[0]:
    dp[0][1] = True

# t의 l개 문자를 만들 수 있는가?
# s oxoxxoxxxo
# oxooxxxo :sub
# xx :coin
for l in range(2, n+1):
    k = 2
    while k >= 0:
        if l-k-1 >= len(sub):
            k -= 1
            continue
        if l > k and dp[l-k-1][k] and t[l-1] == sub[l-k-1]:
            dp[l-k][k] = True
        if k != 0 and dp[l-k][k-1] and t[l-1] == coin[k-1]:
            dp[l-k][k] = True
        k -= 1

if dp[len(sub)][len(coin)]:
    print("YES")
else:
    print("NO")