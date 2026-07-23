class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = 0
        queue = deque([])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j] == 2:
                    queue.append((i, j))
                
        
        while queue and fresh>0:
            for _ in range(len(queue)):
                r,c = queue.popleft()


                if r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]==0:
                    continue 
                
                

                if grid[r][c]==1:
                    grid[r][c]=2
                    queue.append((r,c))
                    fresh -=1


                for dr,dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            
            time += 1

                    
        
        return time if fresh == 0 else -1
            
            
            
            

