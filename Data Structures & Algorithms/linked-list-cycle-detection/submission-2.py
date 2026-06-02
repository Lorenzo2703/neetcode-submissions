# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the list is empty or has only one node, there can be no cycle
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        # Traverse until the fast pointer reaches the end
        while fast and fast.next:
            slow = slow.next          # Move 1 step
            fast = fast.next.next     # Move 2 steps
            
            # If they meet, there is a cycle
            if slow == fast:
                return True
                
        return False
