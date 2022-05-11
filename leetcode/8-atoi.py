"""
https://leetcode.com/problems/string-to-integer-atoi
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. 앞의 공백은 무시
        # 2. 다음 문자가 -, + 인지 확인
        # -> 둘 중 하나라면 읽어라, 마지막 결과의 부호를 결정
        # -> 둘 다 없다면, 마지막 결과는 +
        # 3. non digit 문자까지 계속 읽어라, 끝까지 읽어라 -> 나머지 문자열은 무시
        # 4. 이 digit 들을 정수로 변환, 어떤 digit 도 없다면 0 -> 부호 붙이기
        # 5. 결과값 범위가 벗어나면, 정수를 clamp 해라
        sign = ''
        digit = ''
        s = s.strip()
        for c in s:
            # if c == ' ':
            #     continue
            if c.isdigit():
                digit += c
            elif (c == '+' or c == '-') and not digit and not sign:
                sign = c
            else:
                break
        digit = '0' if not digit else digit

        ret = int(sign + digit)
        m = 2 ** 31
        ret = max(-m, min(m - 1, ret))

        return ret