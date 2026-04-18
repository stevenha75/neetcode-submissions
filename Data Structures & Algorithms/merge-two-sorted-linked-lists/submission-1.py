# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two pointer approach≤
        dummy = ListNode()
        d_ptr = dummy

        # if they both exist -> compare 
        while list1 and list2:
            if list1.val < list2.val:
                d_ptr.next = list1
                list1 = list1.next
            else:
                d_ptr.next = list2
                list2 = list2.next
            d_ptr = d_ptr.next

        d_ptr.next = list1 if list1 else list2 

        return dummy.next if dummy.next else None
