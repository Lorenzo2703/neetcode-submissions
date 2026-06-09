class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]

        for i in range(len(nums)):
            for j in range(i, len(nums)): 
                sub_max = sum(nums[i:j+1])
                maximum = max(maximum, sub_max)

        return maximum