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

        while head:
            queue.append(head)
            head = head.next
        
        # 2. Rebuild the list by popping from ends
        # We start from the head
        head = queue.popleft()
        while queue:
            # Point to the last node
            head.next = queue.pop()
            head = head.next
            
            # Point to the first node (if available)
            if queue:
                head.next = queue.popleft()
                head = head.next
        
        # 3. Ensure the end of the list points to None to avoid cycles
        head.next = None
