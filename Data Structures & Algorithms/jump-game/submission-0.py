class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach=0
        target= len(nums)-1

        for i,v in enumerate(nums):

            if max_reach < i:
                return False

            max_reach=max(max_reach,i+v)

            if max_reach>= target:
                return True

        return max_reach >= target