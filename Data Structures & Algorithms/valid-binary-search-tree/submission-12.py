# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        left_root,right_root=float("-inf"),float("inf")

        if not root:
            return False
    
        # Initialize the queue with the root node
        queue = deque([(root,left_root,right_root)])
        result = []
        
        while queue:
            # Determine the number of nodes at the current level
            level_size = len(queue)
            
            # Process all nodes at this level
            for _ in range(level_size):
                node,min_root,max_root = queue.popleft()
                if not (min_root < node.val < max_root):
                    return False

                # Add children to the queue for the next level
                if node.left:
                    queue.append((node.left,min_root,node.val))
                    
                if node.right:
                    queue.append((node.right,node.val,max_root))

            
            
        return True

