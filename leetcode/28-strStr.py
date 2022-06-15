"""
https://leetcode.com/problems/implement-strstr
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # haystack 에서 needle 이 최초 발생하는 인덱스 리턴
        # -1 : needle 이 존재하지 않을 때
        # needle 이 빈 문자열이라면 무엇을 리턴해야 할까? 0
        # n log n
        if not needle:
            return 0

        i = 0
        n = len(needle)
        while i < len(haystack) - n + 1:
            if haystack[i] == needle[0] and haystack[i:i + n] == needle:
                return i
            i += 1
        return -1
