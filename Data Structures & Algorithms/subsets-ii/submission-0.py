class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort to group duplicates

        def backtrack(start, subset):
            # Add the current subset to results
            res.append(subset.copy())
            
            # Step 2: Iterate through remaining elements
            for i in range(start, len(nums)):
                # Step 3: Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop() # Backtrack

        backtrack(0, [])
        return res