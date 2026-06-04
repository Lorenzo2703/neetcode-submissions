class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        i=0
        lista=[]

        while k<=len(nums):
            lista.append(max(nums[i:k]))
            i+=1
            k+=1
        
        return lista
