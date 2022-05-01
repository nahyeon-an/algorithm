# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # non empty list 2개가 주어진다 -> 각 리스트에는 0이상의 정수가 들어있다
        # 숫자는 역순으로 저장됨, 각 노드는 하나의 숫자를 포함한다 ??
        # 두 숫자를 더한 뒤 링크드 리스트로 합을 리턴해라

        # 각 리스트의 노드의 개수, 리스트의 길이 <= 100
        # 각 노드의 값 : 0~9
        # 각 리스트의 값이 0으로 시작하는 경우는 없다

        # EX3
        # 두 배열의 길이를 맞춰보자 : l2 -> [9, 9, 9, 9, 0, 0, 0]
        # idx == 0 부터 합을 구함 -> 올림은 그다음 인덱스의 값으로 넘김

        # 1. 두 배열의 길이 맞추기
        s = l1.val + l2.val
        head = ListNode(val=s % 10)
        cur = head
        c = s // 10

        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next

            s = l1.val + l2.val + c
            cur.next = ListNode(val=s % 10)
            cur = cur.next

            c = s // 10

        while l1.next:
            l1 = l1.next
            s = l1.val + c
            cur.next = ListNode(val=s % 10)
            cur = cur.next
            c = s // 10

        while l2.next:
            l2 = l2.next
            s = l2.val + c
            cur.next = ListNode(val=s % 10)
            cur = cur.next
            c = s // 10

        if c:
            cur.next = ListNode(val=c)
            cur = cur.next

        return head
