"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # Extract and sort start and end times independently
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        used_rooms = 0
        end_ptr = 0
        
        # Iterate through start times
        for start in starts:
            # If the current meeting starts after or at the time the 
            # earliest ending meeting finishes, we can reuse a room
            if start >= ends[end_ptr]:
                end_ptr += 1
            else:
                # Otherwise, we need a new room
                used_rooms += 1
                
        return used_rooms