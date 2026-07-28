class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo={}

        def backtrack(sums,i):
            if i==len(nums):
                return 1 if sums == target else 0

            if (sums,i) in memo:
                return memo[(sums,i)]
            
            plus = backtrack(sums+nums[i],i+1)
            minus = backtrack(sums-nums[i],i+1)

            memo[(sums,i)]=plus+minus

            return memo[(sums, i)]



        return backtrack(0,0)