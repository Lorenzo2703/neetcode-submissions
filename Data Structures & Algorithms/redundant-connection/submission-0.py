class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        degree = [0] * (len(edges)+1)


        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
            degree[b] += 1


        queue = deque([i for i in range(1,len(edges)+1) if degree[i] == 1])

        while queue:
            curr = queue.popleft()
            degree[curr] -= 1

            

            for neigh in adj[curr]:
                degree[neigh] -= 1
                if degree[neigh] == 1:
                    queue.append(neigh)

        for u, v in reversed(edges):
            if degree[u] > 1 and degree[v] > 1:
                return [u, v]
                
        return []
