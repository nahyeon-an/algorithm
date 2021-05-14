"""
10942 : 팰린드롬
"""
import sys

if __name__ == '__main__':
    # ~ 2000
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())  # ~ 10^6

    dp = [[False for _ in range(n+1)] for _ in range(n+1)]

    # 두개 문자 같으면 true 아니면 false
    for i in range(1, n+1):
        dp[i][i] = True

    for i in range(1, n):
        j = 1
        while j + i <= n:
            if i % 2 == 0:
                dp[j][j+i] = dp[j+1][j+i-1] and (num[j-1] == num[j+i-1])
            else:
                if i == 1:
                    dp[j][j+1] = False
                else:
                    print("j, j+i, num: ", j, j+i, num[j-1], num[j+i-1])
                    dp[j][j+i] = dp[j+1][j+i-1] and (num[j-1] == num[j+i-1])
            j += 1

    for d in dp:
        print(d)

    ans = ''
    for _ in range(m):
        s, e = map(int, sys.stdin.readline().split())
        if dp[s][e]:
            ans += '1\n'
        else:
            ans += '0\n'

    sys.stdout.write(ans)