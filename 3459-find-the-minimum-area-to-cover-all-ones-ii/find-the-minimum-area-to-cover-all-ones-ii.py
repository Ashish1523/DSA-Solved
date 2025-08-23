from math import inf

class Solution:
    def rotateClockWise(self, grid):
        m, n = len(grid), len(grid[0])
        rotated = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - i - 1] = grid[i][j]
        return rotated

    def minimumArea(self, startRow, endRow, startCol, endCol, grid):
        m, n = len(grid), len(grid[0])
        minRow, maxRow = m, -1
        minCol, maxCol = n, -1

        for i in range(startRow, endRow):
            for j in range(startCol, endCol):
                if grid[i][j] == 1:
                    minRow = min(minRow, i)
                    maxRow = max(maxRow, i)
                    minCol = min(minCol, j)
                    maxCol = max(maxCol, j)

        if maxRow == -1:   # no 1s found in subgrid
            return 0
        return (maxRow - minRow + 1) * (maxCol - minCol + 1)

    def utility(self, grid):
        m, n = len(grid), len(grid[0])
        result = inf

        # Case 1: top + bottomLeft + bottomRight
        for rowSplit in range(1, m):
            for colSplit in range(1, n):
                top = self.minimumArea(0, rowSplit, 0, n, grid)
                bottomLeft = self.minimumArea(rowSplit, m, 0, colSplit, grid)
                bottomRight = self.minimumArea(rowSplit, m, colSplit, n, grid)
                result = min(result, top + bottomLeft + bottomRight)

        # Case 2: topLeft + topRight + bottom
        for rowSplit in range(1, m):
            for colSplit in range(1, n):
                topLeft = self.minimumArea(0, rowSplit, 0, colSplit, grid)
                topRight = self.minimumArea(0, rowSplit, colSplit, n, grid)
                bottom = self.minimumArea(rowSplit, m, 0, n, grid)
                result = min(result, topLeft + topRight + bottom)

        # Case 3: top + middle + bottom
        for split1 in range(1, m):
            for split2 in range(split1 + 1, m):
                top = self.minimumArea(0, split1, 0, n, grid)
                middle = self.minimumArea(split1, split2, 0, n, grid)
                bottom = self.minimumArea(split2, m, 0, n, grid)
                result = min(result, top + middle + bottom)

        return result

    def minimumSum(self, grid):
        result = self.utility(grid)
        rotatedGrid = self.rotateClockWise(grid)
        result = min(result, self.utility(rotatedGrid))
        return result
