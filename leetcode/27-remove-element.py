"""
https://leetcode.com/problems/remove-element
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums 에서 모든 val 을 inplace 로 제거
        k = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            if i > j: break
            k += 1
            if i < j and nums[i] == val:
                while j > i >= 0 and nums[j] == val:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            if i == j and nums[i] == val:
                k -= 1
        return k