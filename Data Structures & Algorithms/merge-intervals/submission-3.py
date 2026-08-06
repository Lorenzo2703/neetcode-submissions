class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        i = 0
        while i < len(intervals) - 1:
            # Check if current interval overlaps with the next one
            if intervals[i][1] >= intervals[i + 1][0]:
                # Merge them into the current interval
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                # Delete the next interval since it's now merged
                del intervals[i + 1]
            else:
                # No overlap, move to the next interval
                i += 1

        return intervals


# ---
# -----
#      --

