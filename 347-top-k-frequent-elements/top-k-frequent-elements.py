class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # c=Counter(nums)
        # res1=sorted(c.items(),key=lambda x:(-x[1],x[0]))
        # print(res1)
        # k3=[item[0] for item in res1[:k]]
        # return k3

        # min_heap=[]
        # for i in c:
        #     heapq.heappush(min_heap,c[i])
        #     if len(min_heap)>k:
        #         heapq.heappop(min_heap)
        # m=set(min_heap)
        # ans=[]
        # for i in c:
        #     if c[i] in m:
        #         ans.append(i)
        # return ans
        
        count={}
        freq=[[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res