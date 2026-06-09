class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize with the first element, not 0 or -10
        max_so_far = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Decide: start new or add to existing
            current_sum = max(nums[i], current_sum + nums[i])
            # Update the absolute best seen
            max_so_far = max(max_so_far, current_sum)
            
        return max_so_far