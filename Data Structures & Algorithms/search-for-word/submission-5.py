class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def helper(row, col, ind):
            if ind == len(word):
                return True
            if row<0 or col<0 or row >= rows or col >= cols or board[row][col] != word[ind]:
                return False
            temp = board[row][col]
            board[row][col] = "#"
            found = helper(row+1, col, ind+1) or helper(row-1, col, ind+1) or helper(row, col+1, ind+1) or helper(row, col-1, ind+1)
            board[row][col] = temp
            return found
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and helper(i, j, 0):
                    return True
        return False

