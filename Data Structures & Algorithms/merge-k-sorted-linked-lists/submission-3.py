# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        data = []

        for i in lists:
            while i:
                data.append(i.val)
                i = i.next

        data.sort()
       
        res=ListNode(0)
        cur=res

        for node in data:
            cur.next =ListNode(node)
            cur = cur.next

        return res.next


