class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        for i in range(1,n-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                return i
        return n-1