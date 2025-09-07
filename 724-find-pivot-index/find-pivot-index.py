class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        pref=[0]*n
        pref[0]=nums[0]
        suff=[0]*n
        suff[n-1]=nums[n-1]
        for i in range(1,n):
            pref[i]=nums[i]+pref[i-1]
            suff[n-1-i]+=nums[n-1-i]+suff[n-i]
        # print(pref,suff)
        
        for i in range(n):
            if pref[i]==suff[i]:
                return i
        return -1
