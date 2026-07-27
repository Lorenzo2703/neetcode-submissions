class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1) and board[r][c] == "O":
                    queue.append((r,c))
                    board[r][c] = "T"

        while queue:
            r, c = queue.popleft()
            board[r][c]="T"

            for dn, ds in directions:
                nr, nc = r + dn, c + ds

                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                    board[nr][nc] = "T" 
                    queue.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"


