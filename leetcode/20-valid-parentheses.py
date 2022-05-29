"""
https://leetcode.com/problems/valid-parentheses
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # valid 조건
        # (1) 열린 괄호는 같은 괄호로 닫김
        # (2) 열린 괄호는 반드시 올바른 순서대로 닫혀야 함
        st = []
        for c in s:
            if c in ['(', '{', '[']:
                st.append(c)
            else:
                if not st:
                    return False
                elif c == ')' and st.pop() != '(':
                    return False
                elif c == '}' and st.pop() != '{':
                    return False
                elif c == ']' and st.pop() != '[':
                    return False

        if st:
            return False

        return True