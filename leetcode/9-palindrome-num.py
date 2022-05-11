"""
https://leetcode.com/problems/palindrome-number
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # panlindrome 정수 -> true
        s = str(x)

        # dp[i][j] : s 의 i ~ j 가 팰린드롬인가?
        # dp[i+1][j-1] 이 팰린드롬이고 s[i] == s[j] 이어야 함

        # base case
        length = len(s)
        dp = [[False] * length for _ in range(length)]

        dp[length - 1][length - 1] = True
        for i in range(length - 1):
            dp[i][i] = True
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True

        # for loop
        for l in range(3, length + 1):
            # l : 회문 길이
            for i in range(length - l + 1):
                j = i + l - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True

        return dp[0][length - 1]
