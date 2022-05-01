class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums 의 원소중 합이 target 인 것의 인덱스 출력
        # nums 배열 길이 <= 10^4 -> nlogn

        # 오름차순 정렬 -> 인덱스가 바뀜
        sorted_nums = sorted(nums)

        # 두 포인트
        left, right = 0, len(nums) - 1

        while sorted_nums[left] + sorted_nums[right] != target:
            if sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            else:
                left += 1

        # 원래 인덱스 찾기
        return [i for i, n in enumerate(nums) if n == sorted_nums[left] or n == sorted_nums[right]]
