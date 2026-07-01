# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 'balanced' will track if we've found an imbalance anywhere
        balanced = True

        def dfs(node):
            nonlocal balanced
            if not node or not balanced:
                return 0
            
            # Recursively get heights
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            
            # Check balance at this specific node
            if abs(left_h - right_h) > 1:
                balanced = False
            
            # Return height to the parent
            return max(left_h, right_h) + 1

        dfs(root)
        return balanced