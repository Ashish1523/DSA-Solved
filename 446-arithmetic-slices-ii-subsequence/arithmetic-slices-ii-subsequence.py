class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        result=0
        dp=[defaultdict(int) for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff=nums[i]-nums[j]
                count_at_j=dp[j][diff]
                dp[i][diff]+=count_at_j+1

                result+=count_at_j
        return result

