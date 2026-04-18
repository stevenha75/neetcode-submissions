class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:  # Handle empty list or single node
            return
        
        arr = []
        
        # Convert linked list to array
        while head:
            arr.append(head)
            head = head.next
        
        # Rearrange the nodes in the specified order
        l, r = 0, len(arr) - 1
        while l < r:
            # Link first node and last node
            arr[l].next = arr[r]
            l += 1
            
            if l == r:
                break
            
            # Link last node and next first node
            arr[r].next = arr[l]
            r -= 1
            
        # Set the next of the last node to None
        arr[l].next = None
