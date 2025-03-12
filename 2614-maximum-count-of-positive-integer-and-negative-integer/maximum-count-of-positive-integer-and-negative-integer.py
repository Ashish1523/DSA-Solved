class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_o=0
        count_e=0
        for i in nums:
            if i<0:
                count_o+=1
            elif i>0:
                count_e+=1
        return max(count_o,count_e)