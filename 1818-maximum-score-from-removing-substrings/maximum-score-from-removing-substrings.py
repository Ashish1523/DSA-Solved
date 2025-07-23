class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        st=[]
        ans=0
        st.append(s[0])
        for i in range(1,len(s)):
            if x>=y:
                if s[i]=='b' and st and st[-1]=='a':

                    ans+=x
                    st.pop()
                    continue
            if y>x:
                if s[i]=='a' and st and st[-1]=='b':
                    ans+=y
                    st.pop()
                    continue
            
            st.append(s[i])
        stack=[]
        if st:
            stack.append(st[0])
        for i in range(1,len(st)):
            if x<y:
                if st[i]=='b' and stack and stack[-1]=='a':

                    ans+=x
                    stack.pop()
                    continue
            if y<=x:
                if st[i]=='a' and stack and stack[-1]=='b':
                    ans+=y
                    stack.pop()
                    continue
            
            stack.append(st[i])
        # print(stack)
        return ans
