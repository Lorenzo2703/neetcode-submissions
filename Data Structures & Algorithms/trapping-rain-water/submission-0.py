class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # Initialize our two pointers at the ends of the array
        left, right = 0, len(height) - 1
        
        # Keep track of the tallest bars seen so far from both sides
        left_max, right_max = height[left], height[right]
        area = 0

        while left < right:
            # The smaller boundary determines the water level
            if left_max < right_max:
                left += 1
                # Update the max bar seen from the left
                left_max = max(left_max, height[left])
                # Water trapped is the boundary height minus the current bar height
                area += left_max - height[left]
            else:
                right -= 1
                # Update the max bar seen from the right
                right_max = max(right_max, height[right])
                # Water trapped is the boundary height minus the current bar height
                area += right_max - height[right]

        return area