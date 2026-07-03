# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return []

        queue = deque([root])

        while queue:
            size = len(queue)


            for i in range(size):
                
                node = queue.popleft()
                if i == 0:
                    res.append(node.val)


                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return res
                