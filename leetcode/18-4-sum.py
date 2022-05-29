"""
https://leetcode.com/problems/4sum
"""
class Solution:
    def twoSum(self, nums, target):
        ret = []
        nums = sorted(nums)

        st, en = 0, len(nums) - 1
        while st < en:
            if nums[st] + nums[en] == target:
                ret.append([nums[st], nums[en]])
                st += 1
                en -= 1
            elif nums[st] + nums[en] < target:
                st += 1
            elif nums[st] + nums[en] > target:
                en -= 1

        return ret

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 리턴 : all the unique quadruplets

        # nums 길이 : n (1~200)
        # a, b, c, d 는 모두 다름, distinct
        # nums[a] + nums[b] + nums[c] + nums[d] == target

        ans = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                tmp_list = [nums[i], nums[j]]
                ret = self.twoSum(nums[j + 1:], target - sum(tmp_list))
                for pair in ret:
                    ans.add(tuple(sorted(pair + tmp_list)))

        return list(ans)