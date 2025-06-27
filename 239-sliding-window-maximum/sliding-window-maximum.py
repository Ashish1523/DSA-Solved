class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if not nums or k == 0:
            return []

        result = []
        q = deque()  # store indices

        for i in range(n):
            # Remove indices that are out of the current window
            if q and q[0] == i - k:
                q.popleft()

            # Remove indices whose corresponding values are less than nums[i]
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Start recording max when the first window is fully traversed
            if i >= k - 1:
                result.append(nums[q[0]])

        return result