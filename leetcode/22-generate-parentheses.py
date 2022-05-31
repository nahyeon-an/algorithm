"""
https://leetcode.com/problems/generate-parentheses
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 괄호가 올바르게 짝지어진 모든 콤비네이션

        # n = 1 -> ()
        # n = 2 -> (()), ()(),

        # 아웃풋 문자열 길이 -> 2*n

        from collections import deque
        dq = deque()
        dq.append(("(", 1))
        for i in range(1, 2 * n):
            while len(dq[0][0]) == i:
                cur_string, open_num = dq.popleft()

                if open_num > 0:
                    dq.append((cur_string + "(", open_num + 1))
                    dq.append((cur_string + ")", open_num - 1))
                else:
                    dq.append((cur_string + "(", open_num + 1))

        return [item[0] for item in dq if item[1] == 0]