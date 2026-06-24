class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        if len(nums)<=2:
            return max(nums)

        dp = [0]*len(nums)
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            tmp = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = tmp

        return prev1

