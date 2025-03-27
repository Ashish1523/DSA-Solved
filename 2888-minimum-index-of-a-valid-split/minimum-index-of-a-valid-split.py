class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c=Counter(nums)
        m=max(c.values())
        hi_count=0
        for i in c:
            if c[i]==m:
                hi_count=i
        # print(hi_count)
        count=0
        for i in range(len(nums)):
            if nums[i]==hi_count:
                count+=1
            # print(count,i)
            if count>(i+1)//2 and (m-count)>((len(nums)-i-1))//2:
                return i
        return -1
