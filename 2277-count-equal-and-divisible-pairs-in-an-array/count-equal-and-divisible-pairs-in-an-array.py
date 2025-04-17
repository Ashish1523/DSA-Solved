class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        hash1=defaultdict(list)
        for i in range(len(nums)):
            hash1[nums[i]].append(i)
        count=0
        for w in hash1:
            for i in range(len(hash1[w])):
                for j in range(i+1,len(hash1[w])):
                    if (hash1[w][i]*hash1[w][j]%k==0):
                        count+=1
    
        return count