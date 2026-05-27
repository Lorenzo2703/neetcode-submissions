class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Brute force: sort and for each pair store the range of values, 
        # then put in another list the init value of the range and the last value
        # Time O(nlogn) | Space O(n)

        intervals.sort(key=lambda pair: pair[0])
        output=[intervals[0]]

        for start,end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
