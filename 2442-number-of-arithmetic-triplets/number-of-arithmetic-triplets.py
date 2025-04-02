class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        hashm=defaultdict()
        count=0
        for i in range(len(nums)):
            hashm[nums[i]]=i
        # print(hashm)

        for n in nums:
            if n+diff in hashm and n+2*diff in hashm:
                count+=1
        return count