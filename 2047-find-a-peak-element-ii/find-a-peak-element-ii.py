class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def find_max(ind):
            indi=-1
            ans=-1
            for i in range(m):
                if mat[i][ind]>ans:
                    ans=mat[i][ind]
                    indi=i
            return indi

        m=len(mat)
        n=len(mat[0])
        
        low=0
        high=n-1
        while low<=high:
            mid=(high+low)//2
            i=find_max(mid)
            left=mat[i][mid-1] if mid>0 else -1
            right=mat[i][mid+1] if mid<n-1 else -1
            # print(i,left,right)
            if left<mat[i][mid] and right<mat[i][mid]:
                return [i,mid]
            elif left>mat[i][mid]:
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]