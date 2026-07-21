class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0

        rows = len(grid)
        columns = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):

            if i < 0 or i >= rows or j < 0 or j >= columns or grid[i][j] == 0:
                return 0

          
            grid[i][j] = 0

            current_area = 1

            for r,c in directions:
                grid[i][j] = 0
                current_area += dfs(i + r, j + c)

            return current_area

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    area = max(area, dfs(i, j))

        return area
