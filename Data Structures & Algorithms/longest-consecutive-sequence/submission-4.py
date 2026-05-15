class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums=list(set(nums))
        nums.sort()
        
        maximum=1
        count=1

        for i in range(len(nums)-1):
            print(nums[i]+1,nums[i+1])
            if nums[i]+1==nums[i+1]:
                count+=1
            else:
                count=1
            if maximum<count:
                maximum=count
            

        return maximum