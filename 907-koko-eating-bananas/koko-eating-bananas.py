class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        while(low<=high):
            mid=(low+high)//2
            count=0
            for i in piles:
                count+=math.ceil(i/mid)
            if count<=h:
                high=mid-1
            else:
                low=mid+1
        return low
