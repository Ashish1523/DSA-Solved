class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        arr.append(-1)
        count=1
        ans=-1
        for i in range(len(arr)-1):
            if arr[i]!=arr[i+1]:
                if arr[i]==count:
                    ans=count
                count=1
            else:
                count+=1
        return ans