# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        # Find the second-to-last node
        second_last = head
        while second_last.next.next:
            second_last = second_last.next

        # Move the last node to the second position
        last = second_last.next
        second_last.next = None
        last.next = head.next
        head.next = last

        # Recursively reorder the rest of the list
        self.reorderList(last.next)


        