class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x=[(i[0],i[2]) for i in rectangles]
        y=[(i[1],i[3]) for i in rectangles]
        
        x.sort()
        y.sort()
        def count_non_overlapping(intervals):
            count=0
            prev_end=-1
            for start,end in intervals:
                if prev_end<=start:
                    count+=1
                prev_end=max(prev_end,end)
            return count
        
        return max(
            count_non_overlapping(x),
            count_non_overlapping(y)
        )>=3