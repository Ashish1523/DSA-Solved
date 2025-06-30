class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row, col in zip(matrix, zip(*matrix)):
            print(row,col)
            if len(set(row)) != n or len(set(col)) != n:
                return False
        return True
        
