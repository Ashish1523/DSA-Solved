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
                if mapy[10]:
                    mapy[10]-=1
                elif mapy[5]>2:
                    mapy[5]-=2
                else:
                    return False
            elif change==15:
                if mapy[10] and mapy[5]:
                    mapy[10]-=1
                    mapy[5]-=1
                elif mapy[5]>=3:
                    mapy[5]-=3
                else:
                    print(mapy)
                    return False
        return True