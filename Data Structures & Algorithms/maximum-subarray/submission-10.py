class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum, curr = nums[0],0

        for n in nums:
            if curr <0:
                curr=0
            curr+=n

            maximum = max(curr,maximum)

        return maximum