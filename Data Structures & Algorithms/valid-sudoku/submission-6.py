class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                square = (row // 3) * 3 + (col // 3)
                if (
                    board[row][col] in rows[row]
                    or board[row][col] in columns[col]
                    or board[row][col] in squares[square]
                ):
                    return False
                rows[row].add(board[row][col])

                columns[col].add(board[row][col])

                squares[square].add(board[row][col])

        return True
