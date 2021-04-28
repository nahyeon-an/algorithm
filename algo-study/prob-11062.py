"""
11062 : 카드 게임
"""
import sys

t = int(sys.stdin.readline())

# Top - Down DP (memoization)
while t > 0:
    n = int(sys.stdin.readline())
    card = list(map(int, sys.stdin.readline()[:-1].split()))

    dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(2)]

    def solve(turn, left, right):
        # 근우(turn == 1)의 차례에서 카드의 left ~ right 중 점수의 최선값 반환
        if left == right:
            if turn == 1:
                # 근우의 차례
                return card[left]
            else:
                return 0

        ret = dp[turn][left][right]
        if ret != -1:
            return ret
        else:
            ret = 0

        if turn == 1:
            ret += max(card[left] + solve(0, left+1, right),
                       card[right] + solve(0, left, right-1))
        else:
            # 근우는 점수 획득 안 함
            ret += min(solve(1, left+1, right),
                       solve(1, left, right-1))

        dp[turn][left][right] = ret
        return ret

    print(solve(1, 0, n-1))
    # print(solve(0, 0, n-1))

    t -= 1