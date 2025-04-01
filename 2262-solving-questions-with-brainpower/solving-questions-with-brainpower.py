class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp=[0]*len(questions)
        def back(i):
            if i>=len(questions):
                return 0
            if dp[i]:
                return dp[i]
            points,brainpower=questions[i]
            dp[i]=max(
                back(i+1),points+back(i+1+brainpower)
            )
            return dp[i]
        return back(0)
