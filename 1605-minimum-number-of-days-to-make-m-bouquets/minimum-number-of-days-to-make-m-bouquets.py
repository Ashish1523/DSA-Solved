class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        
        low=1
        high=max(bloomDay)
        ans=high
        while low<=high:
            w=m
            mid=low+(high-low)//2
            count=0
            for i in bloomDay:
                if i<=mid:
                    count+=1
                else:
                    w-=count//k
                    count=0
            w-=count//k
            count=0
            if w<=0:
                # low=mid+1
                ans=min(ans,mid)
                high=mid-1
            else:
                low=mid+1
        return ans