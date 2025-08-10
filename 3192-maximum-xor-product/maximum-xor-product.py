class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD=10**9+7

        xXORa=a>>n
        xXORb=b>>n

        for i in range(n-1,-1,-1):
            ithBit_a=(a>>i)&1
            ithBit_b=(b>>i)&1

            if ithBit_a==ithBit_b:
                xXORa=(xXORa<<1)|1
                xXORb=(xXORb<<1)|1
            else:
                if xXORa<=xXORb:
                    xXORa=(xXORa<<1)|1
                    xXORb=(xXORb<<1)|0
                else:
                    xXORa=(xXORa<<1)|0
                    xXORb=(xXORb<<1)|1
        return (xXORa*xXORb)%MOD
