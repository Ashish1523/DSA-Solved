class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dp=[1]*(n+1)
        hashy=[i for i in range(n)]
        maxi=1
        lastI=0

        nums.sort()
        for i in range(n):
            hashy[i]=i
            for prev in range(i):
                if nums[i]%nums[prev]==0 and 1+dp[prev]>dp[i]:
                    dp[i]=1+dp[prev]
                    hashy[i]=prev
        
            if dp[i]>maxi:
                maxi=dp[i]
                lastI=i

        temp=[]
        temp.append(nums[lastI])
        while hashy[lastI]!=lastI:
            lastI=hashy[lastI]
            temp.append(nums[lastI])
        return temp[::-1]

