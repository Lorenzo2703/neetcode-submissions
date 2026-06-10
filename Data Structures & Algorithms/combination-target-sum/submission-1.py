class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if sum(path)==target:
                res.append(path[:])
                return
                
            if i>len(nums)-1 or sum(path) > target:
                return

            # choice 1: don't include nums[i]
            path.append(nums[i])
            backtrack(i, path)
            path.pop() 
            backtrack(i + 1, path)

        backtrack(0, [])
        return res