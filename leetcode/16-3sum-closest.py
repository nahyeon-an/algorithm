"""
https://leetcode.com/problems/3sum-closest/
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # nums 배열 -> 길이 n
        # target 에 가장 가까운 세 수의 합을 찾아라

        # n^2
        # -4, -1, 1, 2

        nums = sorted(nums)

        ans = nums[0] + nums[1] + nums[-1]
        for i in range(len(nums) - 2):
            st, en = i + 1, len(nums) - 1
            while st < en:
                cur = nums[i] + nums[st] + nums[en]
                if abs(target - ans) > abs(target - cur):
                    ans = cur
                elif target < cur:
                    en -= 1
                else:
                    st += 1

        return ans