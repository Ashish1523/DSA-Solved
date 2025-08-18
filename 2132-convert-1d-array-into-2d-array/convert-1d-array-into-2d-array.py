class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l=len(original)
        if m*n!=l:
            return []
        ans=[]
        val=0
        for i in range(m):
            col=[]
            for j in range(n):
                col.append(original[val])
                val+=1
            ans.append(col)
        return ans