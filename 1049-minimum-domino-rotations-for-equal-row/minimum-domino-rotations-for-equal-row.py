class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        no=-1
        for i in range(1,7):
            c=0
            for j in range(len(tops)):
                if i==tops[j] or i==bottoms[j]:
                    c+=1
                    continue
                else:
                    break
            if c==len(tops):
                no=i
                break
        
        if no==-1:
            return -1
        else:
            return len(tops)-max(tops.count(no),bottoms.count(no))
            