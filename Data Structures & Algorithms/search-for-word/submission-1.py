class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows, columns = len(board), len(board[0])

        def backtrack(r, c, i):

            if i == len(word):
                return True

            if (
                r < 0
                or c < 0
                or r >= rows
                or c >= columns
                or (r, c) in visited
                or word[i] != board[r][c]
            ):
                return

            # choice 1: don't include nums[i]
            visited.add((r,c))

            res=(backtrack(r,c+1,i+1) or
            backtrack(r,c-1,i+1) or
            backtrack(r+1,c,i+1) or
            backtrack(r-1,c,i+1))

            visited.remove((r,c))

            return res

        for i in range(rows):
            for j in range(columns):
                if backtrack(i, j, 0):
                    return True

        return False
