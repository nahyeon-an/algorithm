"""
https://leetcode.com/problems/merge-k-sorted-lists
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeLists(self, list1, list2):
        head = ListNode()
        cur = head

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = ListNode(val=list1.val)
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = ListNode(val=list2.val)
                cur = cur.next
                list2 = list2.next

        while list1:
            cur.next = ListNode(val=list1.val)
            cur = cur.next
            list1 = list1.next

        while list2:
            cur.next = ListNode(val=list2.val)
            cur = cur.next
            list2 = list2.next

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # k 개의 연결리스트가 들어있는 리스트
        # 각각의 연결리스트는 오름차순으로 정렬되어 있음
        # 모든 연결리스트를 merge, 하나의 정렬된 연결리스트로

        # n log n

        # k 개의 헤드, 매번 최솟값 고르기?
        k = len(lists)

        if k == 0:
            return None
        if k == 1:
            return lists[0]
        if k == 2:
            return self.mergeLists(lists[0], lists[1])

        mid = k // 2 + 1
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.mergeLists(left, right)
