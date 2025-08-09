class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        n=len(arr)
        pq=[] 
        for i in range(n):
            heapq.heappush(pq,(arr[i].bit_count(),arr[i]))
        out=[]
        while pq:
            (_,ans)=heapq.heappop(pq)
            out.append(ans)
        return out