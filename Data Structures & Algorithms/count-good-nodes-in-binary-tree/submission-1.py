# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, parent):
            if not node:
                return 0
            
            res = 0
            if parent <= node.val:
                res += 1
                parent = node.val

            res += dfs(node.left, parent)
            res += dfs(node.right, parent)
            
            return res
        
        return dfs(root, root.val - 1)

        # T: O(N)
        # S: O(N)         
        