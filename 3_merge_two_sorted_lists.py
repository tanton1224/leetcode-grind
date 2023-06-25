class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode] -> Optional[L:istNode]):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val > list2.val:
                new.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = tail.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
