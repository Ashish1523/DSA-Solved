class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(pas,total):
            return ((pas+1)/(total+1)) - (pas/total)
        pq=[]
        n=len(classes)
        for pas,total in classes:
            heapq.heappush(pq,(-gain(pas,total),pas,total))
        
        while extraStudents:
            _,pas,total=heapq.heappop(pq)
            pas+=1
            total+=1
            heapq.heappush(pq,(-gain(pas,total),pas,total))
            extraStudents-=1
        ans=0
        for _,pas,total in pq:
            ans+=round(pas/total,5)
        return round(ans/n,5)


