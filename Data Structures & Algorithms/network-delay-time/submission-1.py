class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        pq = [(0, k)]
        visited = set()
        t=0


        for u, v, t in times:
            adj[u].append((v, t))

        while pq:
            distance,node = heapq.heappop(pq)

            if node in visited:
                continue
            
            visited.add(node)
            t = distance
            for element,time in adj[node]:
                if element not in visited:
                    heapq.heappush(pq,(time+distance,element))
        
        return t if len(visited)==n else -1






