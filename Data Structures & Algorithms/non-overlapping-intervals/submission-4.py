class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair:pair[1])

        counter = 0

        comparing = 0

        for i in range(1,len(intervals)):
            
            if intervals[i][0] < intervals[comparing][1]:
                counter += 1
            else:
                comparing = i

            
        return counter