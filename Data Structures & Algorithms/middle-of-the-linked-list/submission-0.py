# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # o(n) + o(n)
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hlen = self.len(head)
        mid = hlen // 2

        i = 0
        res = head
        while i < mid:
            i += 1
            res = res.next
        
        return res

    def len(self, node):
        if not node:
            return 0

        length = 0
        while node:
            length += 1
            node = node.next

        return length
        