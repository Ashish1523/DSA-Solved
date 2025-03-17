class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        has=Counter(nums)
        for i in has:
            if has[i]%2!=0:
                return False
        return True