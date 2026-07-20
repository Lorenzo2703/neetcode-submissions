class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # 1. Sort to handle duplicates

        def backtrack(subs, i, current_sum):
            # Base cases
            if current_sum == target:
                res.append(subs.copy())
                return
            if current_sum > target or i >= len(candidates):
                return 

            # Decision 1: Include candidates[i]
            subs.append(candidates[i])
            backtrack(subs, i + 1, current_sum + candidates[i])
            subs.pop() # Backtrack

            # Decision 2: Exclude candidates[i]
            # Skip duplicates to avoid duplicate combinations
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            
            backtrack(subs, next_i, current_sum)

        backtrack([], 0, 0)
        return res