"""
https://leetcode.com/problems/3sum
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # (1) i != j, i !=k, j!=k -> 서로 다른 인덱스
        # (2) nums[i] + nums[j] + nums[k] == 0
        # 인 모든 [nums[i], nums[j], nums[k]] 쌍

        # nums 길이 <= 3000 -> n log n or n^2

        # (1)을 만족할 수 없음
        if len(nums) < 3:
            return []

        # 정렬
        nums = sorted(nums)

        # 한 숫자를 선택 -> 그것의 음수를 만들 수 있는 두 숫자를 찾기
        ans = set()
        while nums:
            target = nums[0]
            nums = nums[1:]

            st, en = 0, len(nums) - 1

            while st < en:
                cur = nums[st] + nums[en]
                if cur == (-1) * target:
                    tmp = sorted([nums[st], nums[en], target])
                    ans.add(tuple(tmp))
                    st += 1
                    en -= 1
                elif cur < (-1) * target:
                    st += 1
                else:
                    en -= 1

        return ans
