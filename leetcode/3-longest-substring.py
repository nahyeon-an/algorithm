"""
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 가장 긴 부분 문자열 찾기
        # 반복 문자 제외
        # s 길이 <= 5 * 10^4

        sub_str = ''
        max_len = 0
        for i, c in enumerate(s):
            while c in sub_str:
                sub_str = sub_str[1:]
            sub_str += c
            max_len = max(max_len, len(sub_str))

        return max_len
