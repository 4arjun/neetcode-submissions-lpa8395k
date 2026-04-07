class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def helper(row, col, ind, visited):
            if ind == len(word):
                return True
            if row<0 or col<0 or row >= rows or col >= cols:
                return False
            if (row, col) in visited:
                return False
            if board[row][col] != word[ind]:
                return False
            visited.add((row, col))
            bottom = helper(row+1, col, ind+1, visited)
            top = helper(row-1, col, ind+1, visited)
            right = helper(row, col+1, ind+1, visited)
            left = helper(row, col-1, ind+1, visited)
            visited.remove((row, col))
            return bottom or top or left or right
        
        for i in range(rows):
            for j in range(cols):
                if helper(i, j, 0, set()):
                    return True
        return False

