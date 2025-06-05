class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days==1:
            return sum(weights)
        low=max(weights)
        high=sum(weights)
        val=high
        while low<=high:
            mid=low+(high-low)//2
            ans=1
            sum1=0
            for i in weights:
                if sum1+i>mid:
                    ans+=1
                    sum1=i
                else:
                    sum1+=i
            # print(ans,mid,low)
            if ans<=days:
                # print(ans)
                # val=min(val,mid)
                
                high=mid-1
            else:
                low=mid+1
        return low