class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(n)]
        row, col = 0, -1
        rows, cols = 0, 0
        direction = 1
        val = 1
        while rows<n and cols<n:
            for i in range(cols,n):
                col+=direction
                matrix[row][col] = val 
                val+=1
            rows+=1
            for j in range(rows,n):
                row+=direction
                matrix[row][col] = val 
                val+=1
            cols+=1
            direction*=-1
        return matrix

