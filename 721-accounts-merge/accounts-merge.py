class Disjoint:
    def __init__(self,size):
        self.parent=list(range(size))
        self.rank=[0]*size

    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node]= self.find(self.parent[node])
        return self.parent[node]
    
    def unionSet(self,node1,node2):
        xset=self.find(node1)
        yset=self.find(node2)
        if self.rank[xset]<self.rank[yset]:
            self.parent[xset]=yset
        elif self.rank[yset]<self.rank[xset]:
            self.parent[yset]=xset
        else:
            self.parent[yset]=xset
            self.rank[xset]+=1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        ds=Disjoint(n)
        mapy={}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail=accounts[i][j]
                if mail not in mapy:
                    mapy[mail]=i
                else:
                    ds.unionSet(i,mapy[mail])
        
        mergedMail=[[] for _ in range(n)]

        for i in mapy:
            mail=i
            node=ds.find(mapy[i])
            mergedMail[node].append(mail)

        ans=[]
        for i in range(n):
            if len(mergedMail[i])==0:
                continue
            mergedMail[i].sort()
            temp=[]
            temp.append(accounts[i][0])
            for i in mergedMail[i]:
                temp.append(i)
            ans.append(temp)
        return ans

