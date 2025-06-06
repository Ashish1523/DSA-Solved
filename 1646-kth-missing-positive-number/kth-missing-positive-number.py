class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low=0
        n=len(arr)
        high=n-1
        while low<=high:
            mid=low+(high-low)//2
            miss=arr[mid]-(mid+1)
            if miss<k:
                low=mid+1
            else:
                high=mid-1
        return k+high+1
