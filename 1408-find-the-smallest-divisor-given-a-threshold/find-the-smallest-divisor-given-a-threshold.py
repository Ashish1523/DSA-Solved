class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        ans=high
        while(low<=high):
            mid=low+(high-low)//2
            sum1=0
            for i in nums:
                sum1+=math.ceil(i/mid)
            # if sum1==threshold:
            #     print(sum1,ans,mid)
            #     return mid
            if sum1<=threshold:
                print(sum1,ans,mid)
                ans=min(ans,mid)
                high=mid-1
            else:
                low=mid+1
            
        return ans