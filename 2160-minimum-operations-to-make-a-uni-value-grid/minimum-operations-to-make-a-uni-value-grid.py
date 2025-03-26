class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        rem=-1
        res=[]
        for g in grid:
            for i in g:
                if rem==-1:
                    rem=i%x
                if rem!=i%x:
                    return -1
                res.append(i)
        print(res)
        res.sort()
        ind=len(res)//2
        count=0
        for i in res:
            count+=(abs(i-res[ind]))//x
        return count
        
        

        
        