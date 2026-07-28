class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        res = 0

        def backtrack(sums,i):
            if i==len(nums) and sums==target:
                return 1
            if i==len(nums):
                return 0
            
            plus = backtrack(sums+nums[i],i+1)
            minus = backtrack(sums-nums[i],i+1)

            return plus + minus



        return backtrack(0,0)