class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashmap=defaultdict(int)
        for i in range(len(edges)):
            for j in range(len(edges[0])):
                hashmap[edges[i][j]]+=1
        for i in hashmap:
            if hashmap[i]==len(edges):
                return i
        # print(hashmap)