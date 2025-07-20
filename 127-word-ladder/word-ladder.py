class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=deque()
        q.append([beginWord,1])
        st=set(wordList)
        if beginWord in st:
            st.remove(beginWord)

        while q:
            word,steps=q.popleft()
            if word==endWord:
                return steps
            
            for i in range(len(word)):
                word1=list(word)
                for j in range(ord('a'),ord('z')+1):
                    word1[i]=chr(j)
                    k="".join(word1)
                    if k in st:
                        st.remove(k)
                        q.append([k,steps+1])
        return 0


            