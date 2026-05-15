class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for r in range(n):
            if r > 0 and nums[r] == nums[r-1]:
                continue
            
            i = r + 1
            j = n - 1

            while i < j:
                current_sum = nums[r] + nums[i] + nums[j]
                
                if current_sum > 0:
                    j -= 1
                elif current_sum < 0:
                    i += 1
                else:
                    result.append([nums[r], nums[i], nums[j]])
                    
                    i += 1
                    j -= 1
                    
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1

        return result