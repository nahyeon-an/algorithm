"""
12015 : 가장 긴 증가하는 부분 수열 2
"""
import sys

# 1 ~ 1000000
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1

    return start


lis = [nums[0]]
for i in range(1, len(nums)):
    if lis[-1] < nums[i]:
        lis.append(nums[i])
    else:
        pos = binary_search(lis, nums[i], 0, len(lis)-1)
        lis[pos] = nums[i]

print(len(lis))
