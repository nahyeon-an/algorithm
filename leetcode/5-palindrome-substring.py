"""
https://leetcode.com/problems/longest-palindromic-substring
"""
# solution1 : dp (timeout)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 가장 긴 palindrom 부분 문자열 찾기

        # dp[i][j] : s[i:j] 가 팰린드롬일 때 True

        length = len(s)
        dp = [[False] * (length + 1) for _ in range(length + 1)]
        for i in range(length):
            dp[i][i + 1] = True

        # s[i:j]가 팰린드롬인지 검사
        # s[i+1:j-1]이 팰린드롬이고 s[i] == s[j-1] 이어야 함

        ans = s[0]
        for i in range(length - 1):
            # p == 2
            if s[i] == s[i + 1]:
                dp[i][i + 2] = True
                ans = s[i:i + 2]

        for p in range(3, length + 1):
            # p : 팰린드롬 길이
            for i in range(length - p + 1):
                # j = i+p
                if dp[i + 1][i + p - 1] and s[i] == s[i + p - 1]:
                    dp[i][i + p] = True
                    ans = s[i:i + p]

        return ans


# solution2 : expand around center (success)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 가장 긴 palindrom 부분 문자열 찾기

        n = len(s)

        ans = s[0]
        for i in range(n):
            # odd
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > len(ans):
                    ans = s[left:right + 1]
                left -= 1
                right += 1

            # even
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if (right - left + 1) > len(ans):
                    ans = s[left:right + 1]
                left -= 1
                right += 1

        return ans
