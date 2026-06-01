from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build the Adjacency List: map each course to its list of next courses
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            
        visited = set()   # Completely processed nodes (Black)
        rec_stack = set() # Nodes in current recursion path (Gray)

        def dfs(node):
            # Base Case: If it's in the current path, we found a cycle!
            if node in rec_stack:
                return True
            # Base Case: If we already fully explored this node before, it's safe
            if node in visited:
                return False

            # Mark as visiting
            rec_stack.add(node)

            # Recurse through actual neighbors from our adjacency map
            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True # Pass the cycle signal up the call stack

            # Backtrack: mark node as fully safe
            rec_stack.remove(node)
            visited.add(node)
            
            return False

        # 2. Outer loop across ALL course IDs to catch disconnected sub-graphs
        for course in range(numCourses):
            if course not in visited:
                if dfs(course):
                    return False # Cycle detected! We cannot finish.
                    
        return True # Checked everything, no cycles found. We can finish!