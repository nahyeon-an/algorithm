"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums : 정수 배열, non decreasing 정렬되어 있다
        # 동일한것 제거, 유니크 원소 한번씩만 나타나게
        # 원소들의 순서는 그대로 유지되어야 함
        # return : k
        # inplace 변환해야 함

        insertPointer = 0
        k = 1

        for checkPointer in range(1, len(nums)):
            if nums[insertPointer] != nums[checkPointer]:
                k += 1
                insertPointer += 1
                nums[insertPointer] = nums[checkPointer]

        return k