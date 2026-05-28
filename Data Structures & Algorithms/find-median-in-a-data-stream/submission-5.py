class MedianFinder:
    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        self.heap.append(num)

    def findMedian(self) -> float:
        length = len(self.heap)
        self.heap.sort()

        if (length % 2) != 0:

            return self.heap[length//2]
        
        return ((self.heap[length//2]+self.heap[length//2 -1])/2)

