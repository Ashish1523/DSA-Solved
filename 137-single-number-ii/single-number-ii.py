class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for k in range(32):
            temp=1<<k
            countOnes=0
            for num in nums:
                if num & temp!=0:
                    countOnes+=1
            if countOnes%3==1:
                res=res | temp
        
        if res>=2**31:
            res-=2**32
        return res
