class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while curr or stack:
            # 1. Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Pop the node (this is the next smallest element)
            curr = stack.pop()
            k -= 1
            
            # 3. If k reaches 0, we found our target
            if k == 0:
                return curr.val
            
            # 4. Move to the right child
            curr = curr.right
            
        return -1 # Should not reach here for valid input