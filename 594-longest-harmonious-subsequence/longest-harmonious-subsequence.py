class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #2-pointer
        # nums.sort()
        # j=0
        # ans=0
        # print(nums)
        # for i in range(len(nums)):
        #     while nums[i]-nums[j]>1:
        #         j+=1
        #     if nums[i]-nums[j]==1:
        #         ans=max(ans,i-j+1)
        # return ans

        #hashing
        mapy=Counter(nums)
        ans=0
        for i in mapy:
            if i+1 in mapy:
                leng=mapy[i]+mapy[i+1]
                ans=max(ans,leng)
        return ans