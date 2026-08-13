class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []
       
        intervals.sort(key=lambda pair:pair[0])

        out=[intervals[0]]

        for i in range(1,len(intervals)):
            start_int, end_int = intervals[i][0], intervals[i][1]
            start_out, end_out = out[-1][0], out[-1][1]

            if start_int <= end_out:
                out[-1][1] = max(out[-1][1], end_int)
            else:
                out.append([start_int,end_int])


        
        return out