# 11053 : 가장 긴 증가하는 부분 수열
n = int(input())  # <= 1000
a = input().split(" ")

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start


cnt = 1
nums = [int(a[0])]
for i in range(1, len(a)):
    if int(a[i]) > nums[cnt - 1]:
        nums.append(int(a[i]))
        cnt += 1
    else:
        pos = binary_search(nums, int(a[i]), 0, cnt)
        nums[pos] = int(a[i])

print(len(nums))

