class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        nums.insert(0,1)
        nums.append(1)
        # dp=[[-1 for _ in range(n+1)] for _ in range(n+1)]
        # def burst(i,j):
        #     if i>j:
        #         return 0
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     maxi=float('-inf')
        #     for k in range(i,j+1):
        #         val=nums[i-1]*nums[k]*nums[j+1]+burst(i,k-1)+burst(k+1,j)
        #         maxi=max(maxi,val)
        #     dp[i][j]=maxi
        #     return maxi
        # return burst(1,n)

        dp=[[0 for _ in range(n+2)] for _ in range(n+2)]

        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j:
                    continue
                maxi=float('-inf')
                for k in range(i,j+1):
                    val=nums[i-1]*nums[k]*nums[j+1]+dp[i][k-1]+dp[k+1][j]
                    maxi=max(maxi,val)
                dp[i][j]=maxi
        # print(dp)
        return dp[1][n]
                