class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        mat=[[] for i in range(numRows)]
        c=0
        j=0
        for i in range(len(s)):
            mat[j].append(s[i])
            if c==0:
                j+=1
                if j==numRows:
                    c=1
                    j-=1
            if c==1:
                j-=1
                if j==-1:
                    c=0
                    j+=2
        out=""
        for i in range(len(mat)):
            for ele in mat[i]:
                out+=ele
        return out

        