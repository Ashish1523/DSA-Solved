class Solution:
    def sumZero(self, n: int) -> List[int]:
        val=n//2
        ans=[]
        while val:
            ans.append(val)
            ans.append(-val)
            val-=1
        if n%2:
            ans.append(0)
        return ans
