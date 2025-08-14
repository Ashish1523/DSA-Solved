class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapy={}
        n=len(fruits)
        r=0
        l=0
        ans=0
        while r<n:
            if fruits[r] not in mapy:
                mapy[fruits[r]]=1
            else:
                mapy[fruits[r]]+=1
            if len(mapy)>2:
                # print(l)
                mapy[fruits[l]]-=1
                if mapy[fruits[l]]==0:
                    del mapy[fruits[l]]
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans

