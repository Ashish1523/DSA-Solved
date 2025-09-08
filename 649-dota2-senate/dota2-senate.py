class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D=deque()
        R=deque()
        n=len(senate)
        for i,c in enumerate(senate):
            if c=="R":
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            Rval=R.popleft()
            Dval=D.popleft()
            if Rval<Dval:
                R.append(Rval+n)
            else:
                D.append(Dval+n)
        return "Radiant" if R else "Dire"