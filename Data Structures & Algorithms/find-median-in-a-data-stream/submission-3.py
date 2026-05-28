class MedianFinder:
    def __init__(self):
        self.heapq = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heapq, num)

    def findMedian(self) -> float:
        length = len(self.heapq)
        self.heapq.sort()

        if (length % 2) != 0:

            return self.heapq[length//2]
        
        return ((self.heapq[length//2]+self.heapq[length//2 -1])/2)

