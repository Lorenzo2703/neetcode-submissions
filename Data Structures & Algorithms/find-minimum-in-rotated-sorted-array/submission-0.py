class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        i=0
        z=len(nums)-1

        while nums[z]<nums[i]:
            z-=1
            i-=1

        return nums[i]