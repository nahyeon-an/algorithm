"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 리턴 : 숫자가 나타낼 수 있는 모든 가능한 조합 (순서 상관 없음)
        from itertools import product

        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        # digits 길이 -> 0 ~ 4 -> max: 4 ^ 4 = 2 ^ 8 = 256

        if not digits:
            return []

        cur = letters[int(digits[0])]
        for i in range(1, len(digits)):
            cur = product(cur, letters[int(digits[i])])
            cur = [''.join(pair) for pair in cur]

        return cur