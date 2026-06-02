# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Store all nodes in a deque
        queue = deque()
        curr = head
        while curr:
            queue.append(curr)
            curr = curr.next
        
        # 2. Rebuild the list by popping from ends
        # We start from the head
        curr = queue.popleft()
        while queue:
            # Point to the last node
            curr.next = queue.pop()
            curr = curr.next
            
            # Point to the first node (if available)
            if queue:
                curr.next = queue.popleft()
                curr = curr.next
        
        # 3. Ensure the end of the list points to None to avoid cycles
        curr.next = None