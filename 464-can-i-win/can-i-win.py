class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal<=0:
            return True
        netTotal=(maxChoosableInteger*(maxChoosableInteger+1))//2
        if netTotal<desiredTotal:
            return False
        
        memo={}

        def can_win(choices,total):
            state=tuple(choices)
            if state in memo:
                return memo[state]
            if choices[-1]>=total:
                memo[state]=True
                return True
            for i in range(len(choices)):
                if not can_win(choices[:i]+choices[i+1:],total-choices[i]):
                    memo[state]=True
                    return True
            memo[state]=False
            return False
        
        return can_win(list(range(1,maxChoosableInteger+1)),desiredTotal)