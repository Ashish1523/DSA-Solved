class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans=0

        for house in houses:
            left=0
            right=len(heaters)-1
            while left<right:
                mid=(left+right)//2
                if heaters[mid] < house:
                    left=mid+1
                else:
                    right=mid
            dist=abs(heaters[left]-house)
            if left>0:
                dist=min(dist,abs(heaters[left-1]-house))
            ans=max(ans,dist)
        return ans