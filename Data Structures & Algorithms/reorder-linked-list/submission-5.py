class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:  # Handle empty list or single node
            return
        
        # Step 1: Convert linked list to array
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        
        # Step 2: Rearrange nodes
        l, r = 0, len(nodes) - 1
        while l < r: # avoid loops
            # Link the current left node to the current right node
            nodes[l].next = nodes[r]
            l += 1
            
            if l == r:  # Check if they meet in the middle
                break
            
            # Link the current right node to the next left node
            nodes[r].next = nodes[l]
            r -= 1
        
        # Step 3: Ensure the last node points to None
        nodes[l].next = None