"""
https://leetcode.com/problems/longest-common-prefix
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        i = 0  # 문자열 내의 문자의 인덱스
        while True:
            c = strs[0][i] if i < len(strs[0]) else ''
            for st in strs:
                if i >= len(st) or st[i] != c:
                    return ans
            i += 1
            ans += c

        return ans