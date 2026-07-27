"""
In-degree count: Count how many prerequisites each course needs (in_degree array).  
Start with 0 prerequisites: Put all courses that need 0 prerequisites into a queue (they can be taken immediately). 
Process and Unlock: Pop a course, add it to your output list, and "unlock" the courses that depend on it by reducing their prerequisite count by 1. 
If any course hits 0 prerequisites, push it to the queue.  
Check for cycles: If your final output list contains all the courses, you have your order. 
If not (meaning a cycle trapped some courses), return an empty list.

"""


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
                if in_degree[neigh] == 0:
                    queue.append(neigh)

        return out if len(out) == numCourses else []
