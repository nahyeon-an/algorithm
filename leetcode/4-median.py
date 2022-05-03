"""
https://leetcode.com/problems/median-of-two-sorted-arrays
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 정렬된 배열 num1, num2 에서
        # merged 배열에서 median 구하기

        m = len(nums1)
        n = len(nums2)

        # 각각 nums1 배열과 num2 배열의 인덱스
        i, j = 0, 0

        # n + m 이 홀수 -> (n+m) // 2 인덱스에 해당하는 값 가져오기
        # n + m 이 짝수 -> (n+m) // 2, (n+m) // 2 - 1 인덱스에 해당하는 값의 평균

        # merged arr 배열의 인덱스
        k = -1
        arr = []
        while i < m and j < n:
            if k == (n + m) // 2:
                break

            if nums1[i] < nums2[j]:
                arr.append(nums1[i])
                k += 1
                i += 1
            else:
                arr.append(nums2[j])
                k += 1
                j += 1

        while i < m:
            if k == (n + m) // 2:
                break
            arr.append(nums1[i])
            i += 1
            k += 1

        while j < n:
            if k == (n + m) // 2:
                break
            arr.append(nums2[j])
            j += 1
            k += 1

        if (n + m) % 2 == 0:
            return (arr[k] + arr[k - 1]) / 2
        else:
            return arr[k]
