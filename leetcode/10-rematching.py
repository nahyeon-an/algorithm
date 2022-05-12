"""
https://leetcode.com/problems/regular-expression-matching
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s : 입력 스트링
        # p : 패턴
        # . 과 * 을 지원하는 정규식을 구현
        # . : 모든 싱글 문자
        # * : 0 또는 더 많은 선행 요소

        # base case : 패턴이 없을 때, 남은 스트링도 없음
        if not p:
            return not s

        first_match = s and p[0] in (s[0], '.')  # 첫번째 문자가 일치하는가

        if len(p) >= 2 and p[1] == '*':
            return (first_match and self.isMatch(s[1:], p)) or (self.isMatch(s, p[2:]))
        else:
            return first_match and self.isMatch(s[1:], p[1:])
