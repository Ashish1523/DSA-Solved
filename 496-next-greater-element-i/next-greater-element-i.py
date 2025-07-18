class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1Idx={n:i for i,n in enumerate(nums1)}
        # res=[-1]*len(nums1)
        # stack=[]
        # for i in range(len(nums2)):
        #     cur=nums2[i]
        #     while stack and cur >stack[-1]:
        #         val=stack.pop()
        #         idx=nums1Idx[val]
        #         res[idx]=cur
        #     if cur in nums1Idx:
        #         stack.append(cur)
        # return res


        # h=defaultdict(int)
        # h1={}
        # for
        # # n1=set(nums1)
        # for i in range(len(nums2)):
        #     # if nums2[i] not in n1:
        #     #     continue
        #     max1=-1
        #     for j in range(i+1,len(nums2)):
        #         if nums2[j]>nums2[i]:
        #             max1=nums2[j]
        #             break
        #     h[nums2[i]]=max1
        # # print(h)
        # res=[]
        # for i in nums1:
        #     res.append(h[i])
        # return res

        valIdx={}
        for i in range(len(nums1)):
            valIdx[nums1[i]]=i
        stack=[]
        res=[-1]*len(nums1)
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            # print(stack)
            if len(stack)==0:
                if nums2[i] in valIdx:
                    res[valIdx[nums2[i]]]=-1
            else:
                if nums2[i] in valIdx:
                    res[valIdx[nums2[i]]]=stack[-1]
            stack.append(nums2[i])
        return res