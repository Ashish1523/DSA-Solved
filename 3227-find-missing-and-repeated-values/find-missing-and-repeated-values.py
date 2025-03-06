class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res1=[]
        for i in range(len(grid)):
            for j in range(len(grid)):
                res1.append(grid[i][j])

        res1.sort()
        res2=[]
        for i in range(len(res1)-1):
            if(res1[i]==res1[i+1]):
                res2.append(res1[i])
                break
        for i in range(1,len(res1)+1):
            if i not in res1:
                res2.append(i)
                break
        
        return res2
       
        
