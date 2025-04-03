class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res,val_m,diff_m=0,0,0
        for n in nums:
            res=max(res,diff_m*n)
            diff_m=max(diff_m,val_m-n)
            val_m=max(val_m,n)
        return res