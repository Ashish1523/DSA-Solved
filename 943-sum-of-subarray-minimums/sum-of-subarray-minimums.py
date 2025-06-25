from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # Previous Less Element (strictly less)
        def prevLess(arr):
            stack = []
            prev = [-1] * n
            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                prev[i] = stack[-1] if stack else -1
                stack.append(i)
            return prev

        # Next Less or Equal Element (to avoid double counting)
        def nextLessEqual(arr):
            stack = []
            next_ = [n] * n
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                next_[i] = stack[-1] if stack else n
                stack.append(i)
            return next_

        prev = prevLess(arr)
        next_ = nextLessEqual(arr)

        result = 0
        for i in range(n):
            left = i - prev[i]
            right = next_[i] - i
            result += arr[i] * left * right
            result %= MOD

        return result
