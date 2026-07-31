class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        curr = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, nums[i]+i)

            if curr == i:
                curr = farthest
                jumps += 1  
                if curr >= len(nums) - 1:
                    break
            
        
        return jumps