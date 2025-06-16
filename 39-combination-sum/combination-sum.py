# from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, total, cur):
            if len(res) >= 150:  # Stop if we've reached the output limit
                return
            if total == target:
                res.append(cur[:])
                return
            for i in range(start, len(candidates)):
                if total + candidates[i] > target:
                    break  # Early pruning
                cur.append(candidates[i])
                dfs(i, total + candidates[i], cur)
                cur.pop()

        dfs(0, 0, [])
        return res
