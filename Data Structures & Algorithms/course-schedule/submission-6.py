class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list: prereq -> list of courses that depend on it
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            # edge: prereq -> course
            adj[prereq].append(course)
            indegree[course] += 1

        # Queue of courses with no prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        taken = 0

        while q:
            u = q.popleft()
            taken += 1

            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        # If we can take all courses, no cycle
        return taken == numCourses