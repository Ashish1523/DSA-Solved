class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        if n<=k:
            return sum(cardPoints)
        rsum=0
        lsum=0
        for i in range(k):
            rsum+=cardPoints[i]
        ans=rsum
        i=k-1
        j=n-1
        while i>=0:
            rsum-=cardPoints[i]
            lsum+=cardPoints[j]
            ans=max(ans,rsum+lsum)
            i-=1
            j-=1
        return ans