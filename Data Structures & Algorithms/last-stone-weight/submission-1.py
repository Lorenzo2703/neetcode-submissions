class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []

        for i in stones:
            heapq.heappush(maxheap,-i)

        while len(maxheap)>1:
            y = -1*heapq.heappop(maxheap)
            x = -1*heapq.heappop(maxheap)

            if y > x:
                heapq.heappush(maxheap,-1*( y-x))


        return -maxheap[0] if maxheap else 0

