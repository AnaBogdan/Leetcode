# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        cnt = 0
        dummy = head

        while dummy:
            cnt += 1
            dummy = dummy.next
        if cnt == n:
            return head.next
        dummy2 = ListNode()
        dummy2.next = head
        for i in range(cnt - n):
            dummy2 = dummy2.next
        dummy2.next=dummy2.next.next
        return head

