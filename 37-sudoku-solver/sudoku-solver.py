from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        empty = []

        # Initialize the sets and record empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    val = board[i][j]
                    row[i].add(val)
                    col[j].add(val)
                    box[(i // 3, j // 3)].add(val)

        def backtrack(index):
            if index == len(empty):
                return True
            i, j = empty[index]
            for c in "123456789":
                if c in row[i] or c in col[j] or c in box[(i // 3, j // 3)]:
                    continue
                board[i][j] = c
                row[i].add(c)
                col[j].add(c)
                box[(i // 3, j // 3)].add(c)

                if backtrack(index + 1):
                    return True

                # Backtrack
                board[i][j] = "."
                row[i].remove(c)
                col[j].remove(c)
                box[(i // 3, j // 3)].remove(c)
            return False

        backtrack(0)
