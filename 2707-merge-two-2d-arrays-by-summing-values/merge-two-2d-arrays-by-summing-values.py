class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res=defaultdict(int)
        for id1,val in nums1:
            res[id1]+=val
        for id2,val in nums2:
            res[id2]+=val
        
        f_res=[]
        res=dict(sorted(res.items()))
        for key in res:
            f_res.append([key,res[key]])
        return f_res