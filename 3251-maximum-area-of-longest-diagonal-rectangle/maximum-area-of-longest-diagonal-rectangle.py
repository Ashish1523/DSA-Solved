class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag=0
        area=0
        mapy=defaultdict(list)
        for l,b in dimensions:
            newdiag=(l**2+b**2)**0.5
            if newdiag>=diag:
                diag=newdiag
                mapy[diag].append(l*b)
            
        return max(mapy[diag])