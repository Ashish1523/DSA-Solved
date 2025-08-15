class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        l=1
        h=n-2
        while l<=h:
            mid=(l+h)//2
            # print(mid)
            if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]>arr[mid]:
                h=mid-1
            else:
                l=mid+1
        return n-1