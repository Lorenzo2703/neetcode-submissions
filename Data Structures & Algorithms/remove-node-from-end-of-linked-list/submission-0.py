# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        curr = head


        while end and n > 0:
            end = end.next
            n -= 1
        
        if not end:
            return head.next

        while end.next:
            end = end.next
            curr = curr.next

        curr.next = curr.next.next

        return head

