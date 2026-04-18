# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # init pointers
        left = dummy
        right = head

        # create a gap of size n
        while n > 0:
            right = right.next
            n -= 1

        # -> once right is null -> left will point to the target
        while right:
            right = right.next
            left = left.next
        
        # remove value in left.next
        left.next = left.next.next

        return dummy.next # return the head of the updated list