# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""

        while l1:
            n1 = str(l1.val) + n1
            l1=l1.next

        while l2:
            n2 = str(l2.val) + n2
            l2 = l2.next

        res = int(n1)+int(n2)

        s_res = str(res)

        dummy = ListNode(0)
        current = dummy
        
        # Iterate backwards through the string to create the list
        for i in range(len(s_res) - 1, -1, -1):
            current.next = ListNode(int(s_res[i]))
            current = current.next
            
        return dummy.next



