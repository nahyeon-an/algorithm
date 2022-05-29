"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lengthOfList(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.lengthOfList(head)

        prev = None
        cur = head
        for i in range(length):
            if i == (length - n):
                # remove
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next
                cur = cur.next
                continue
            prev = cur
            cur = cur.next

        return head