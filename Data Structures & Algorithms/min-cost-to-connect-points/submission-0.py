class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        visited = set()
        n = len(points)

        heap = [(0, 0)]

        total = 0

        while len(visited) < n:
            cost, i = heapq.heappop(heap)

            if i in visited:
                continue

            visited.add(i)

            total += cost
            
            x1, y1 = points[i]

            for j in range(n):
                if j not in visited:
                    x2,y2 = points[j]
                    dst = abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(heap,(dst,j))
                    


        return total