class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path=[]
        res=[]
        def palindrome(str,index,i):
            low=index
            high=i
            while low<high:
                if str[low]!=str[high]:
                    return False
                low+=1
                high-=1
            return True
        
        def generate(index):
            if index==len(s):
                res.append(path[:])
                return
            for i in range(index,len(s)):
                if palindrome(s,index,i):
                    path.append(s[index:i+1])
                    generate(i+1)
                    path.pop()
        
        generate(0)
        return res