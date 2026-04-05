class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in row[i] or val in col[j] or val in box[(i//3)*3+(j//3)]:
                    return False
                row[i].add(val)
                col[j].add(val)
                box[(i//3)*3+(j//3)].add(val)
        return True
