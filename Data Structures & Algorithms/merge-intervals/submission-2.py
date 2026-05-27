class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Brute force:  after sorting
        # we keep track of the last merged interval
        # if the current interval overlaps with it, we merge them
        # otherwise, we start a new interval
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
