class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def count_citation(val):
            count=0
            for i in range(n):
                if citations[i]>=val:
                    count+=1
            return count
        citations.sort()
        n=len(citations)
        low=1
        high=n
        while low<=high:
            mid=(low+high)//2
            if count_citation(mid)>=mid:
                low=mid+1
            else:
                high=mid-1
        return high
