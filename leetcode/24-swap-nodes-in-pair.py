"""
https://leetcode.com/problems/swap-nodes-in-pairs
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 모든 인접 노드들을 스왑
        # 노드의 값을 변경하면 안 됨

        idx = 0
        prev = head
        cur = head.next if head else None

        ans = ListNode()
        pt = ans

        while prev and cur:
            pt.next = ListNode(val=cur.val)
            pt = pt.next
            pt.next = ListNode(val=prev.val)
            pt = pt.next

            prev = cur.next
            cur = prev.next if prev else None

        if prev:
            pt.next = ListNode(val=prev.val)
            pt = pt.next

        if cur:
            pt.next = ListNode(val=cur.val)
            pt = pt.next

        return ans.next