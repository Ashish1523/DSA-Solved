class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # pref=[0]*len(nums)
        low=max(nums)
        high=sum(nums)
        while(low<=high):
            mid=low+(high-low)//2
            var=1
            sum1=0
            for i in nums:
                if sum1+i>mid:
                    var+=1
                    sum1=i
                else:
                    sum1+=i
                if var>k:
                    break
            if var>k:
                low=mid+1
            else:
                high=mid-1
        return low
        