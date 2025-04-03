class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[[1],[1,1]]
        if rowIndex==0 or rowIndex==1:
            return row[rowIndex]

        for i in range(2,rowIndex+1):
            res=[1]
            for j in range(1,len(row[i-1])):
                res.append(row[i-1][j-1]+row[i-1][j])
            res.append(1)
            row.append(res)
        return row[rowIndex]