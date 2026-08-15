class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = {}

        for a in range(9):
            for s in range(9):
                if board[a][s] in row_check.values():
                    return False
                if board[a][s] != ".":
                    row_check[a, s] = board[a][s]
            row_check.clear()


        column_check = {}
        for idx in range(9):
            for j in range(9):
                if board[j][idx] in column_check.values():
                    return False
                if board[j][idx] != ".":
                    column_check[j, idx] = board[j][idx]
            column_check.clear()

        square_check = {}

        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                seen = set()
                for r in range(start_row, start_row + 3):
                    for c in range(start_col, start_col + 3):
                        if board[r][c] in seen:
                            return False
                        if board[r][c] != ".":
                            seen.add(board[r][c])


        return True
