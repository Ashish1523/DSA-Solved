class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # flips=0
        # while (a | b | c):
        #     if c&1==0:
        #         if a&1==1:#right shift
        #             flips+=1
        #         if b&1==1:
        #             flips+=1
        #     else:
        #         if a&1==0 and b&1==0:
        #             flips+=1
        #     a=a>>1
        #     b=b>>1
        #     c=c>>1
        # return flips
        temp=(a|b)^c
        return (temp).bit_count()+(temp&(a&b)).bit_count()

                
        