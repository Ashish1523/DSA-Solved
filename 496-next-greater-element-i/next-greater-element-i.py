class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h=defaultdict(int)
        for i in range(len(nums2)):
            max1=-1
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    max1=nums2[j]
                    break
            h[nums2[i]]=max1
        # print(h)
        res=[]
        for i in nums1:
            res.append(h[i])
        return res