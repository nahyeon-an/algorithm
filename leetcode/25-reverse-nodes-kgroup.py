"""
https://leetcode.com/problems/reverse-nodes-in-k-group
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseGroup(self, head, k):
        vals = []

        while head and k > 0:
            vals.append(head.val)
            head = head.next
            k -= 1

        reverse_head = ListNode()
        cur = reverse_head
        for val in vals[::-1]:
            cur.next = ListNode(val=val)
            cur = cur.next

        return reverse_head.next, cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k : 양의 정수, 연결리스트의 길이보다 작거나 같음

        cur = head
        checkPointer = head
        cnt = 1

        ans_head, ans_tail = None, None

        while checkPointer:
            if cnt == k:
                reversed_head, reversed_tail = self.reverseGroup(cur, k)
                if not ans_head:
                    ans_head = reversed_head
                    ans_tail = reversed_tail
                else:
                    ans_tail.next = reversed_head
                    ans_tail = reversed_tail

                checkPointer = checkPointer.next
                cur = checkPointer
                cnt = 1
            else:
                checkPointer = checkPointer.next
                cnt += 1

        while cur:
            # 남은거 연결
            ans_tail.next = cur
            ans_tail = ans_tail.next
            cur = cur.next

        return ans_head