class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        j=len(heights)
        i=0
        while i<j:
            area=max(min(heights[i],heights[j-1])*(j-1-i),area)
            if heights[i]<heights[j-1]:
                i+=1
            else:
                j-=1

        return area