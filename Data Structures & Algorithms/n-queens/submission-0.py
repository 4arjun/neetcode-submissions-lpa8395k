class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        result = []
        cols = set()
        diag = set()
        anti_diag = set()
        def isSafe(r, c):
            if c in cols or (r-c) in diag or (r+c) in anti_diag:
                return False
            return True

        def helper(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            for c in range(n):
                if isSafe(row, c):
                    board[row][c] = "Q"
                    cols.add(c)
                    diag.add(row-c)
                    anti_diag.add(row+c)
                    helper(row+1)
                    board[row][c] = "."
                    cols.remove(c)
                    diag.remove(row-c)
                    anti_diag.remove(row+c)
        helper(0)
        return result

