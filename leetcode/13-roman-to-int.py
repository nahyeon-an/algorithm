"""
https://leetcode.com/problems/roman-to-integer
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        i = 0
        ans = 0
        while i < len(s):
            c = s[i]

            if i + 1 < len(s) and c == 'I' and (s[i + 1] in ['V', 'X']):
                ans += (roman.get(s[i + 1]) - roman.get(c))
                i += 2
            elif i + 1 < len(s) and c == 'X' and (s[i + 1] in ['L', 'C']):
                ans += (roman.get(s[i + 1]) - roman.get(c))
                i += 2
            elif i + 1 < len(s) and c == 'C' and (s[i + 1] in ['D', 'M']):
                ans += (roman.get(s[i + 1]) - roman.get(c))
                i += 2
            else:
                ans += roman.get(c)
                i += 1

        return ans