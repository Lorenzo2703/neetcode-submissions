class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        max_length = 0
        n = len(nums)

        left = 0

        dp = [1]*n

        for i in range(1, n):
            for j in range(0, i):
                # If we find an element smaller than the current one
                if nums[i] > nums[j]:
                    # Update dp[i] to be the max length found so far
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)