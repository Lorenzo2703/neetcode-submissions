class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Dummy node protects against edge cases where left = 1
        dummy = ListNode(0, head)
        
        # 1. Move 'prev' to the node just before the 'left' position
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
            
        # 2. Reverse the sublist from left to right
        current = prev.next
        prev_sub = None
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev_sub
            prev_sub = current
            current = next_node
            
        # 3. Reconnect the reversed sublist to the rest of the list
        tail = prev.next
        tail.next = current  # 'current' points to the node at index right + 1
        prev.next = prev_sub  # 'prev_sub' is the new head of the reversed section
        
        return dummy.next