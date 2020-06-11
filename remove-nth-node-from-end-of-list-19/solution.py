# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        right_ptr = dummy
        left_ptr = dummy

        # Create a cushion of n between the pointers
        for _ in range(n+1):
            right_ptr = right_ptr.next

        # Now that cushion is established, increment both pointers until right_ptr reaches the end of the list
        while right_ptr:
            right_ptr = right_ptr.next
            left_ptr = left_ptr.next

        left_ptr.next = left_ptr.next.next

        return dummy.next
