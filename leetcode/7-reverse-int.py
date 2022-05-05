class Solution:
    def reverse(self, x: int) -> int:
        # 32 bit 정수 x
        # x 의 역순 숫자를 리턴
        # 리버스 값이 범위를 벗어나면 0을 리턴

        minus = 1
        if x < 0:
            minus = -1
            x *= minus
        elif x == 0:
            return 0

        s = ''
        while x:
            s += str(x % 10)
            x //= 10

        ans = int(s) * minus
        n = 2 ** 31
        if (-1) * n <= ans <= n - 1:
            return ans
        else:
            return 0
