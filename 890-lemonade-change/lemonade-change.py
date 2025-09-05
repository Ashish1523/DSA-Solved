class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mapy={5:0,10:0,20:0}
        n=len(bills)
        for i in range(n):
            change=bills[i]-5
            mapy[bills[i]]+=1
            if change==5:
                if mapy[5]==0:
                    return False
                mapy[5]-=1
            elif change==10:
                if mapy[5]<2 and mapy[10]==0:
                    return False
                if mapy[10]:
                    mapy[10]-=1
                else:
                    mapy[5]-=2
            elif change==15:
                if (mapy[5]<3 and mapy[10]==0):
                    return False
                if mapy[10]!=0 and mapy[5]==0:
                    return False
                if mapy[10]:
                    mapy[10]-=1
                    mapy[5]-=1
                else:
                    mapy[5]-=3
        return True