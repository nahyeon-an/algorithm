"""
https://leetcode.com/problems/container-with-most-water
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # hegith : n 길이의 정수 배열
        # n 개의 세로선
        # i번째 세로선의 두 엔드포인트 -> (i, 0), (i, height[i])
        # 가장 많이 물을 담을 수 있는 2개의 선을 찾아라
        # 리턴 : 컨테이너가 담을 수 있는 물의 최대량

        # n : 2 <= <= 10^5
        # 복잡도 : n log n, n

        # container -> line[j], line[i] -> (j - i) * min(line[j], line[i])

        ans = -1
        st, en = 0, len(height) - 1
        while st < en:
            size = (en - st) * min(height[st], height[en])
            ans = max(ans, size)
            if height[st] < height[en]:
                st += 1
            else:
                en -= 1

        return ans