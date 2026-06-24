class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        if len(nums)<=2:
            return max(nums)

        prev2 = 0
        prev1 = 0

        for i in range(len(nums)):
            tmp = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = tmp

        return prev1

