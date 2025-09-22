class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        mapy=defaultdict(int)
        maxy=0
        for num in nums:
            mapy[num]+=1
            maxy=max(maxy,mapy[num])
        
        count=0
        for key in mapy:
            if mapy[key]==maxy:
                count+=mapy[key]
        return count