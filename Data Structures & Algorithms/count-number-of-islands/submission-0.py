class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        rows= len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def recursiveFind(r,c):
            if (r < 0 or c < 0 or r >= rows or
                    c >= cols or grid[r][c] == "0"
                ):
                    return
            grid[r][c] = "0"
            for dr, dc in directions:
                recursiveFind(r + dr, c + dc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    num += 1
                    
                    recursiveFind(i,j)


        

        return num