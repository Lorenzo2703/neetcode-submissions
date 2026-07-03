# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,maxs):
            if not node:
                return 0

            res = 1 if node.val >= maxs else 0

            maxs = max(maxs, node.val)
            res += dfs(node.left, maxs)
            res += dfs(node.right,maxs)
            return res
        
        return dfs(root,root.val)
