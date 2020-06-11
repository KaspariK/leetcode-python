# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create list to old merged lists. Initialize with placeholder value
        merged_list = ListNode(-1)

        # This is the return. We create this to "preserve" the head of the merged_list
        merged_list_head = merged_list

        while l1 and l2:
            if l1.val < l2.val:
                merged_list.next = l1
                l1 = l1.next
            else:
                merged_list.next = l2
                l2 = l2.next

            merged_list = merged_list.next

        merged_list.next = l1 or l2

        # Return head.next because the first item is a placeholder (-1)
        return merged_list_head.next
