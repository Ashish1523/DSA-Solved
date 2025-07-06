class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2=nums2
        self.hash1=Counter(nums1)
        self.hash2=Counter(nums2)
    def add(self, index: int, val: int) -> None:
        self.hash2[self.nums2[index]]-=1
        self.nums2[index]+=val
        self.hash2[self.nums2[index]]+=1

    def count(self, tot: int) -> int:
        count=0
        # for i in range(len(self.nums1)):
        #     for j in range(len(self.nums2)):
        #         if self.nums1[i]+self.nums2[j]==tot:
        #             count+=1
        for i in self.hash1:
            if tot-i in self.hash2:
                count+=(self.hash1[i]*self.hash2[tot-i])
        
        return count

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)