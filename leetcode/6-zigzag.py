class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 지그재그 패턴을로 문자를 쓴다
        # 주어진 row 수에서

        # 그리고 왼쪽에서 오른쪽으로, 위에서 아래로 행을 옮기며 읽는다

        # arr[i] : i 번째 행에 들어갈 문자 리스트
        if numRows == 1:
            return s

        arr = ['' for _ in range(numRows)]

        r = 0
        flag = True  # T -> +, F -> -
        for c in s:
            arr[r] += c

            if flag:
                r += 1
            else:
                r -= 1

            if r == numRows - 1:
                flag = False
            elif r == 0:
                flag = True

        return ''.join(arr)
