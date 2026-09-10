class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        j = 0
        for i in range(len(nums)):
            # If the window size exceeds k, shrink it from the left
            if i - j > k:
                j += 1
            
            # Check all elements currently inside the window [j, i-1]
            for x in range(j, i):
                if nums[x] == nums[i]:
                    return True
        return False