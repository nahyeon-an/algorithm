# 2473 : 세 용액
n = int(input()) # 3 ~ 5000
vals = list(map(int, input().split(" ")))
vals.sort() # n lg n

# def binary_search(start, target, j):
#     global vals
#
#     end = len(vals) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if vals[mid] > target:
#             end = mid-1
#         elif vals[mid] < target:
#             start = mid+1
#         else:
#             break
#
#     # return index
#     # print(start, end)
#     # print("---------")
#     if end == j:
#         return start
#     elif start >= len(vals):
#         return end
#     else:
#         if abs(target - vals[start]) > abs(target - vals[end]):
#             return end
#         else:
#             return start
#
# ''' 반례
# 5
# -5 -1 2 3 4
# '''
# ans = 3000000005
# for i in range(len(vals) - 1):
#     for j in range(i+1, len(vals)-1):
#         t = - vals[i] - vals[j]
#         idx = binary_search(j+1, t, j)
#         # idx = binary_search(0, t, i, j)
#         # print(i, j, idx, t)
#         # print(vals[i], vals[j], vals[idx])
#         # print()
#         if vals[idx] == t:
#             l = str(vals[i]) + " " + str(vals[j]) + " " + str(vals[idx])
#             break
#         if abs(vals[i]+vals[j]+vals[idx]) < ans:
#             ans = abs(vals[i]+vals[j]+vals[idx])
#             l = str(vals[i]) + " " + str(vals[j]) + " " + str(vals[idx])
#
# print(l)

import sys
maximum = sys.maxsize
i1, i2, i3 = -1, -1, -1
for i in range(len(vals)):
    left = i+1
    right = n-1

    while left < right:
        s = vals[i] + vals[left] + vals[right]

        if abs(s) < maximum:
            maximum = abs(s)
            i1 = i
            i2 = left
            i3 = right

        if s < 0:
            left += 1
        elif s > 0:
            right -= 1
        else:
            i1 = i
            i2 = left
            i3 = right
            break

print(vals[i1], vals[i2], vals[i3])