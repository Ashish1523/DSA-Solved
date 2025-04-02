class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res,i_m,d_m=0,0,0
        for n in nums:
            res=max(res,d_m*n)
            d_m=max(d_m,i_m-n)
            i_m=max(i_m,n)
        return res

