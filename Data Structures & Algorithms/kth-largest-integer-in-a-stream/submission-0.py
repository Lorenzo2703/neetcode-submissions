class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        
        # Add all numbers and maintain heap size at k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            # Replace the smallest element if val is larger
            heapq.heapreplace(self.heap, val)
        
        return self.heap[0]