class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq=[]
        for i in arr:
            heapq.heappush(pq,[-abs(x-i),-i])
            if len(pq)>k:
                heapq.heappop(pq)

        ans=[]
        for _,val in pq:
            ans.append(-val)
        return sorted(ans)
            