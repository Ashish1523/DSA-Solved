class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # normalize k

        # reverse the entire list
        self.reverse(nums, 0, n - 1)
        # reverse first k elements
        self.reverse(nums, 0, k - 1)
        # reverse remaining elements
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1



    

                