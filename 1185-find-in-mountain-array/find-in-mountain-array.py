# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n=mountainArr.length()
        low=1
        high=n-2
        ans=0
        while low<=high:
            mid=(low+high)//2
            prev=mountainArr.get(mid-1)
            curr=mountainArr.get(mid)
            nex=mountainArr.get(mid+1)
            if prev<curr and nex<curr:
                ans=mid
                break
            elif prev>curr:
                high=mid-1
            else:
                low=mid+1
        # print(ans)
        low=0
        high=ans
        while low<=high:
            mid=(low+high)//2
            # print(mid)
            val=mountainArr.get(mid)
            if val==target:
                return mid
            elif val>target:
                high=mid-1
            else:
                low=mid+1
        # prin
        low=ans+1
        high=n-1
        while low<=high:
            mid=(low+high)//2
            val=mountainArr.get(mid)
            if val==target:
                return mid
            elif val>target:
                low=mid+1
            else:
                high=mid-1
        return -1
    

