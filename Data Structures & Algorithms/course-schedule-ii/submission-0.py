class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        out = []

        while queue:
            curr = queue.popleft()
            out.append(curr)

            for neigh in adj[curr]:
                in_degree[neigh] -= 1
                if in_degree[neigh]==0:
                    queue.append(neigh)


        return out if len(out) == numCourses else []