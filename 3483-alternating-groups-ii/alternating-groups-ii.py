class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        alt=0
        val_count=0

        for j in range(k-1):
            if colors[j]!=colors[(j+1)%n]:
                val_count+=1
            
        if val_count==k-1:
            alt+=1

        for i in range(1,n):
            if colors[i-1]!=colors[(i)%n]:
                val_count-=1

            if colors[(i+k-2)%n]!=colors[(i+k-1)%n]:
                val_count+=1

            if val_count==k-1:
                alt+=1

        return alt
        

