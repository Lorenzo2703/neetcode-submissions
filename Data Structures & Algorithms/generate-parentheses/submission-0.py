class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(opened,closed, sub):
            
            if opened==closed==n:
                res.append(sub)
                return
            
            if closed>opened:
                return

            if opened>n:
                return
            
            backtrack(opened+1,closed,sub+"(")

            backtrack(opened,closed+1,sub+")")

        backtrack(0,0,"")

        return res