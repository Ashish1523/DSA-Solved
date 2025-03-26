class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=max(candies)
        res=[]
        for i in candies:
            if i+extraCandies>=ans:
                res.append(True)
            else:
                res.append(False)
        return res