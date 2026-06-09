class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize with the first element, not an arbitrary number
        maximum = nums[0] 

        for i in range(len(nums)):
            current_sub_sum = 0
            for j in range(i, len(nums)):
                current_sub_sum += nums[j]
                # Update maximum if the current sub_sum is higher
                if current_sub_sum > maximum:
                    maximum = current_sub_sum

        return maximum