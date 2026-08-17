class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        fresh = 0
        minutes = 0
        queue = deque([])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        if fresh == 0:
            return 0

        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dr, dc in directions:
                    nr, nc = x + dr, y + dc
                    
                    # Check if the neighbor is valid and is a fresh orange
                    if 0 <= nr < ROWS and 0 <= nc < COLUMNS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Turn it rotten
                        fresh -= 1  # One less fresh orange
                        queue.append((nr, nc)) # Add to queue for the next minute wave

        return minutes if fresh == 0 else -1
