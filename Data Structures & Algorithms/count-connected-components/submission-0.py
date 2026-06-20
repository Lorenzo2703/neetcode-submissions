class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj=defaultdict(list)

        count=0
        visited = set()

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
                visited.add(node)
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        dfs(neighbor)
            
            # Iterate through all nodes 0 to n-1
        for i in range(n):
            if i not in visited:
                # Found a new component
                count += 1
                dfs(i)

        return count